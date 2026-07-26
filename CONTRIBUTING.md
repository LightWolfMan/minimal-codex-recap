# Como contribuir

Obrigado por ajudar a manter o Minimal Codex Recap pequeno e previsível.

## Princípios

- Preserve a invocação exclusivamente manual.
- Manter o skill sem dependências de execução nem código executável.
- Usar somente a conversa atual como fonte.
- Nunca adicionar leitura de arquivos, chamadas de ferramentas, memória
  persistente, acesso à rede ou alterações de estado ao fluxo do recap.
- Manter o contrato de saída padrão com exatamente três linhas.
- Preferir respostas honestas a progresso inferido ou inventado.

## Desenvolvimento

1. Crie uma ramificação a partir de `main`.
2. Faça a menor alteração que resolva o problema.
3. Execute:

   ```bash
   python tests/validate_skill.py
   ```

4. Se `skills/recap/SKILL.md` ou `skills/recap/agents/openai.yaml` mudar
   intencionalmente, atualize os hashes aprovados no teste e nos dois arquivos
   README.
5. Explique qualquer mudança de comportamento em `CHANGELOG.md`.

Solicitações de alteração devem incluir um exemplo concreto de conversa e o
resultado esperado em três linhas.
