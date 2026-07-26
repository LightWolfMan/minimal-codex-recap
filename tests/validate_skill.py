#!/usr/bin/env python3
"""Dependency-free contract checks for Minimal Codex Recap."""

from __future__ import annotations

import hashlib
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "recap" / "SKILL.md"
OPENAI_YAML = ROOT / "skills" / "recap" / "agents" / "openai.yaml"

EXPECTED_HASHES = {
    SKILL: "F4CE8B4B0B7DB1516A5C397FD3BAB904DC03C6DDF17CA3A4BF2222CA3D0E8467",
    OPENAI_YAML: "1A2DB46B36959BB31CC0F4046A59CC4CBFB77DB53030C0542D91B04ED9D188D8",
}

EXPECTED_FALLBACKS = (
    "Onde paramos: nenhum trabalho anterior foi identificado nesta conversa.",
    "Pendente: nada identificado.",
    "Próxima ação: aguardar nova instrução.",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest().upper()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def validate_skill() -> None:
    skill_text = SKILL.read_text(encoding="utf-8")
    yaml_text = OPENAI_YAML.read_text(encoding="utf-8")

    frontmatter = re.match(r"\A---\n(.*?)\n---\n", skill_text, re.DOTALL)
    require(frontmatter is not None, "SKILL.md must start with YAML frontmatter")
    metadata = frontmatter.group(1)
    require(re.search(r"^name:\s*recap\s*$", metadata, re.MULTILINE) is not None, "skill name must be recap")
    require(re.search(r"^description:\s*.+$", metadata, re.MULTILINE) is not None, "description is required")

    require("Não chamar\nferramentas" in skill_text, "tool prohibition is missing")
    require("não ler arquivos" in skill_text, "file-read prohibition is missing")
    require("não consultar memória persistente" in skill_text, "persistent-memory prohibition is missing")
    require("não alterar\nestado" in skill_text, "state-change prohibition is missing")
    require("Produzir exatamente três linhas" in skill_text, "three-line output contract is missing")

    for fallback in EXPECTED_FALLBACKS:
        require(fallback in skill_text, f"fallback missing: {fallback}")

    require("allow_implicit_invocation: false" in yaml_text, "implicit invocation must remain disabled")
    require('default_prompt: "Use $recap' in yaml_text, "default prompt must mention $recap")

    for path, expected in EXPECTED_HASHES.items():
        actual = sha256(path)
        require(actual == expected, f"SHA-256 mismatch for {path.name}: {actual}")


if __name__ == "__main__":
    validate_skill()
    print("Minimal Codex Recap contract validation passed.")
