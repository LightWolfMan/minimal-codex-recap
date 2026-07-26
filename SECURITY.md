# Política de segurança

## Escopo

O Minimal Codex Recap não contém código executável em tempo de execução. Seu
limite de segurança é o contrato de instruções presente em `SKILL.md`.

Relate qualquer comportamento que faça `$recap`:

- chamar uma ferramenta ou comando;
- ler um arquivo ou memória persistente;
- acessar a rede;
- alterar estado local ou remoto;
- revelar informações que não estejam na conversa atual;
- executar por invocação implícita.

## Como relatar

Não abra um relato público se ele contiver dados sensíveis da conversa. Use o
fluxo de aviso privado de segurança do GitHub para este repositório.

Inclua a versão do Codex, a superfície usada (App ou CLI), a invocação exata, a
saída sanitizada e se o skill foi instalado globalmente ou apenas no projeto.
