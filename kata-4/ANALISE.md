# Análise — Kata 4

## Decisões de tratamento de dados

Durante o desenvolvimento do pipeline, foram tomadas as seguintes decisões:

### 1. Datas inconsistentes
Os campos de data foram normalizados utilizando parsing flexível, aceitando múltiplos formatos:
- DD/MM/AAAA
- AAAA-MM-DD
- timestamps

Datas inválidas foram convertidas para `null` para evitar falhas no pipeline.

---

### 2. Valores monetários
Valores com vírgula como separador decimal foram convertidos para ponto, garantindo compatibilidade com operações numéricas.

Valores nulos foram tratados como 0 para evitar quebra de cálculos agregados.

---

### 3. Registros órfãos (orphan records)
Registros de entregas com `id_pedido` inexistente foram removidos.

Essa decisão foi tomada para garantir consistência referencial no dataset final.

Além disso, evita inconsistências em relatórios financeiros e indicadores de entrega, garantindo que apenas pedidos válidos sejam considerados nos cálculos.

Alternativamente, esses registros poderiam ser armazenados para análise de inconsistência entre sistemas.

---

### 4. Campos nulos
- Registros com `id_cliente` nulo foram mantidos, mas resultam em dados incompletos no join
- Campos obrigatórios ausentes não interrompem o pipeline, mas são propagados como nulos no dataset final.

- Essa decisão prioriza resiliência do pipeline, evitando falhas completas por dados inconsistentes, ao custo de possíveis lacunas nos indicadores.

---

### 5. Normalização de cidades
Os nomes de cidades foram padronizados com:
- remoção de espaços extras
- conversão para lowercase
- capitalização (title case)

Exemplo:
- "sao paulo" → "Sao Paulo"
- "SAO PAULO" → "Sao Paulo"

---

## Idempotência do pipeline

O pipeline é idempotente.

Ou seja, executar o processo múltiplas vezes com os mesmos dados de entrada produz o mesmo resultado.

Isso ocorre porque:
- não há mutação incremental dos dados
- não há dependência de estado externo
- o output é sempre gerado do zero
- o pipeline não realiza escrita incremental nem depende de timestamps de execução, evitando efeitos colaterais entre execuções

---

## Escalabilidade (10 milhões de linhas)

Para grandes volumes de dados, seriam necessárias mudanças:

### Melhorias propostas:
- Utilização de processamento distribuído (ex: Spark)
- Leitura em chunks (pandas chunking)
- Uso de banco de dados para joins ao invés de memória
- Armazenamento em formatos mais eficientes (Parquet)
- Paralelização do processamento
- Separação entre ingestão, transformação e camada de consumo (arquitetura de dados em camadas)

---

## Testes recomendados

Para garantir qualidade, seriam implementados:

### Testes unitários:
- Conversão de datas em múltiplos formatos
- Normalização de cidades
- Conversão de valores monetários

### Testes de integração:
- Pipeline completo com dataset pequeno controlado
- Verificação do output final esperado

### Testes de qualidade de dados:
- Validação de schema
- Verificação de nulls em colunas críticas
- Consistência entre tabelas (integridade referencial)

### Testes de regressão:
- Garantir que alterações no pipeline não modifiquem resultados históricos de forma inesperada

---

## Considerações finais

O pipeline foi projetado priorizando clareza e robustez, com tratamento explícito das principais inconsistências de dados.

A solução garante consistência nos dados consolidados e pode ser facilmente evoluída para ambientes produtivos com melhorias de infraestrutura e escalabilidade.