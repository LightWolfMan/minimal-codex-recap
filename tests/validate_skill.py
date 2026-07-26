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
    SKILL: "3EEB98C2DED080701B4C6440641258F358745DDB65B89FF6823C3BC80073A604",
    OPENAI_YAML: "43493E9963711B7F4342B6A6AB50B4F2922CE35C78CB2E9C40B7CB73FA18E756",
}

RESPOSTAS_SEGURAS_PT = (
    "Onde paramos: nenhum trabalho anterior foi identificado nesta conversa.",
    "Pendente: nada identificado.",
    "Próxima ação: aguardar nova instrução.",
)

RESPOSTAS_SEGURAS_EN = (
    "Where we stopped: no previous work was identified in this conversation.",
    "Pending: nothing identified.",
    "Next action: wait for a new instruction.",
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
    exigir("usar inglês quando" in texto_skill, "falta a regra de seleção do inglês")
    exigir("usar português quando" in texto_skill, "falta a regra de seleção do português")
    exigir(
        re.search(r"se ainda não\s+houver evidência, usar português", texto_skill) is not None,
        "falta o idioma padrão",
    )
    exigir("mistura de idiomas" in texto_skill, "falta a proibição de misturar idiomas")
    exigir("Where we stopped: <one objective sentence>" in texto_skill, "falta o rótulo inglês da primeira linha")
    exigir("Next action: <one concrete action>" in texto_skill, "falta o rótulo inglês da terceira linha")

    for resposta_segura in RESPOSTAS_SEGURAS_PT + RESPOSTAS_SEGURAS_EN:
        exigir(resposta_segura in texto_skill, f"falta resposta segura: {resposta_segura}")

    exigir("allow_implicit_invocation: false" in texto_yaml, "a invocação implícita deve continuar desativada")
    exigir('default_prompt: "Use $recap' in texto_yaml, "o prompt padrão deve mencionar $recap")
    exigir("português ou inglês" in texto_yaml, "a descrição da interface deve informar os dois idiomas")

    for caminho, esperado in HASHES_ESPERADOS.items():
        atual = sha256(caminho)
        exigir(atual == esperado, f"SHA-256 divergente em {caminho.name}: {atual}")


if __name__ == "__main__":
    validar_skill()
    print("Validação de contrato do Minimal Codex Recap concluída com sucesso.")
