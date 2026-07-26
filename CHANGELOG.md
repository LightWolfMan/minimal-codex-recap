# Histórico de alterações

Todas as alterações relevantes deste projeto são documentadas neste arquivo.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/)
e o projeto adota [Versionamento Semântico](https://semver.org/lang/pt-BR/).

## [1.0.2] - 2026-07-26

### Alterado

- Português brasileiro definido como idioma principal do repositório.
- README em inglês movido para `README.en.md`, acessível pelo link destacado
  **In English**.
- Inspiração no `/recap` do Claude Code reconhecida de forma explícita, junto
  ao aviso de independência e ausência de afiliação com a Anthropic.
- Documentação, integração contínua e imagem demonstrativa localizadas.
- Redação interna do skill localizada como “respostas seguras”, sem alteração
  do contrato ou do comportamento.
- Tradução informativa da licença MIT adicionada sem substituir o texto
  jurídico canônico.

### Preservado

- O contrato de três linhas, as respostas seguras literais e a ativação
  exclusivamente manual permanecem idênticos aos da versão 1.0.1.
- `skills/recap/agents/openai.yaml` permanece byte a byte idêntico.

## [1.0.1] - 2026-07-26

### Corrigido

- Skill instalável movido para `skills/recap/`, garantindo que o Skills CLI
  copie somente os dois arquivos necessários em execução, sem documentação nem
  testes do repositório.
- GitHub Actions atualizado para as versões oficiais v7 baseadas em Node 24.

## [1.0.0] - 2026-07-26

### Adicionado

- Invocação exclusivamente manual por `$recap` no Codex App e no Codex CLI.
- Contrato fixo de três linhas para o estado da conversa atual.
- Respostas literais seguras para conversas sem evidências suficientes.
- `policy.allow_implicit_invocation: false`.
- Validação de contrato sem dependências no Windows e no Ubuntu.
- Documentação em português brasileiro e inglês.

[1.0.2]: https://github.com/LightWolfMan/minimal-codex-recap/releases/tag/v1.0.2
[1.0.1]: https://github.com/LightWolfMan/minimal-codex-recap/releases/tag/v1.0.1
[1.0.0]: https://github.com/LightWolfMan/minimal-codex-recap/releases/tag/v1.0.0
