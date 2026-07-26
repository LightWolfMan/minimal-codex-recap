---
name: recap
description: Recapitular manualmente a conversa atual em três linhas, no idioma dominante da conversa entre português e inglês, indicando onde o trabalho parou, o que está pendente e a próxima ação concreta. Usar somente quando o usuário invocar explicitamente $recap.
---

# Recap

Resumir somente o que estiver estabelecido na conversa atual. Não chamar
ferramentas, não ler arquivos, não consultar memória persistente e não alterar
estado.

Escolher um único idioma para toda a resposta:

- usar inglês quando as mensagens substantivas mais recentes do usuário
  estiverem claramente em inglês;
- usar português quando estiverem claramente em português;
- em caso de ambiguidade, seguir o idioma dominante da conversa; se ainda não
  houver evidência, usar português.

Produzir exatamente três linhas, sem introdução, conclusão, título, lista,
bloco de código ou mistura de idiomas.

Em português:

- `Onde paramos: <uma frase objetiva>`
- `Pendente: <uma frase objetiva>`
- `Próxima ação: <uma ação concreta>`

Em inglês:

- `Where we stopped: <one objective sentence>`
- `Pending: <one objective sentence>`
- `Next action: <one concrete action>`

Fundamentar cada linha apenas em evidências da conversa. Não presumir que uma
ação foi concluída, que um teste passou ou que um arquivo mudou quando isso não
estiver explícito.

Quando não houver evidência suficiente, usar estas respostas seguras
literalmente no idioma escolhido.

Em português:

- `Onde paramos: nenhum trabalho anterior foi identificado nesta conversa.`
- `Pendente: nada identificado.`
- `Próxima ação: aguardar nova instrução.`

Em inglês:

- `Where we stopped: no previous work was identified in this conversation.`
- `Pending: nothing identified.`
- `Next action: wait for a new instruction.`
