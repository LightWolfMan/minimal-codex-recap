---
name: recap
description: Recapitular manualmente a conversa atual em três linhas, indicando onde o trabalho parou, o que está pendente e a próxima ação concreta. Usar somente quando o usuário invocar explicitamente $recap.
---

# Recap

Resumir somente o que estiver estabelecido na conversa atual. Não chamar
ferramentas, não ler arquivos, não consultar memória persistente e não alterar
estado.

Produzir exatamente três linhas, sem introdução, conclusão, título, lista ou
bloco de código:

```text
Onde paramos: <uma frase objetiva>
Pendente: <uma frase objetiva>
Próxima ação: <uma ação concreta>
```

Fundamentar cada linha apenas em evidências da conversa. Não presumir que uma
ação foi concluída, que um teste passou ou que um arquivo mudou quando isso não
estiver explícito.

Quando não houver evidência suficiente, usar estes fallbacks literalmente:

- `Onde paramos: nenhum trabalho anterior foi identificado nesta conversa.`
- `Pendente: nada identificado.`
- `Próxima ação: aguardar nova instrução.`
