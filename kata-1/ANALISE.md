# Análise — Kata 1

## Estrutura de dados

Optei por utilizar uma lista (`List<Patient>`) com ordenação customizada utilizando LINQ.

Essa abordagem foi escolhida por sua simplicidade e legibilidade, considerando o volume esperado de dados no contexto do problema.

---

## Complexidade do algoritmo

A ordenação utiliza `OrderBy`, que possui complexidade média de:

O(n log n)

Para volumes pequenos e médios, essa abordagem é eficiente e suficiente.

Caso a lista tivesse 1 milhão de pacientes, alternativas como estruturas de dados baseadas em heap (priority queue) poderiam ser consideradas para otimizar inserções e remoções.

---

## Interação entre regras 4 e 5

As regras podem se combinar.

Exemplo:
Paciente com 15 anos e urgência MÉDIA:

1. Urgência base: MÉDIA (2)
2. Regra 5 (menor de idade): +1 → ALTA (3)
3. Regra 4 não se aplica (não é idoso)

Resultado final: ALTA

---

## Extensibilidade

Para suportar novas regras, a lógica de cálculo de prioridade poderia ser extraída para uma estratégia mais flexível, como:

- Strategy Pattern
- Rule Engine simples (lista de regras aplicáveis)

Isso permitiria adicionar novas regras sem modificar diretamente o método principal, reduzindo acoplamento e melhorando a manutenibilidade.