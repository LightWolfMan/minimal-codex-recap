#!/usr/bin/env python3
"""Validações de contrato sem dependências do Minimal Codex Recap."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


RAIZ = Path(__file__).resolve().parents[1]
SKILL = RAIZ / "skills" / "recap" / "SKILL.md"
OPENAI_YAML = RAIZ / "skills" / "recap" / "agents" / "openai.yaml"

HASHES_ESPERADOS = {
    SKILL: "C2B3DF20255725547597A5A262727995D1A594F0B66539638D2F66895BA0D856",
    OPENAI_YAML: "1A2DB46B36959BB31CC0F4046A59CC4CBFB77DB53030C0542D91B04ED9D188D8",
}

RESPOSTAS_SEGURAS_ESPERADAS = (
    "Onde paramos: nenhum trabalho anterior foi identificado nesta conversa.",
    "Pendente: nada identificado.",
    "Próxima ação: aguardar nova instrução.",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def exigir(condicao: bool, mensagem: str) -> None:
    if not condicao:
        raise AssertionError(mensagem)


def validar_skill() -> None:
    texto_skill = SKILL.read_text(encoding="utf-8")
    texto_yaml = OPENAI_YAML.read_text(encoding="utf-8")

    frontmatter = re.match(r"\A---\n(.*?)\n---\n", texto_skill, re.DOTALL)
    exigir(frontmatter is not None, "SKILL.md deve começar com frontmatter YAML")
    metadados = frontmatter.group(1)
    exigir(re.search(r"^name:\s*recap\s*$", metadados, re.MULTILINE) is not None, "o nome do skill deve ser recap")
    exigir(re.search(r"^description:\s*.+$", metadados, re.MULTILINE) is not None, "a descrição é obrigatória")

    exigir("Não chamar\nferramentas" in texto_skill, "falta a proibição de ferramentas")
    exigir("não ler arquivos" in texto_skill, "falta a proibição de leitura de arquivos")
    exigir("não consultar memória persistente" in texto_skill, "falta a proibição de memória persistente")
    exigir("não alterar\nestado" in texto_skill, "falta a proibição de alteração de estado")
    exigir("Produzir exatamente três linhas" in texto_skill, "falta o contrato de saída em três linhas")

    for resposta_segura in RESPOSTAS_SEGURAS_ESPERADAS:
        exigir(resposta_segura in texto_skill, f"falta resposta segura: {resposta_segura}")

    exigir("allow_implicit_invocation: false" in texto_yaml, "a invocação implícita deve continuar desativada")
    exigir('default_prompt: "Use $recap' in texto_yaml, "o prompt padrão deve mencionar $recap")

    for caminho, esperado in HASHES_ESPERADOS.items():
        atual = sha256(caminho)
        exigir(atual == esperado, f"SHA-256 divergente em {caminho.name}: {atual}")


if __name__ == "__main__":
    validar_skill()
    print("Validação de contrato do Minimal Codex Recap concluída com sucesso.")
