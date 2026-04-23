# Plano de Ação Técnico — Kata 3


## Seção 1 — Diagnóstico

### 1. Endpoint lento (8–12 segundos)

**Causa raiz provável:**

* Consultas ineficientes no banco (falta de índices, N+1 queries)
* Ausência de paginação
* Possível sobrecarga de processamento na aplicação

**Risco:**

* Técnico: degradação de performance e escalabilidade
* Negócio: perda de usuários e impacto na experiência do cliente

**Classificação:**
Urgente e Importante

---

### 2. Pedidos duplicados

**Causa raiz provável:**

* Falta de controle de idempotência
* Ausência de validação transacional no banco
* Possível concorrência sem controle

**Risco:**

* Técnico: inconsistência de dados
* Negócio: prejuízo financeiro e retrabalho operacional

**Classificação:**
Urgente e Importante

---

### 3. Alteração direta em produção (sem PR/teste)

**Causa raiz provável:**

* Ausência de processo de CI/CD
* Falta de governança de código
* Pressão operacional sem controle

**Risco:**

* Técnico: introdução de bugs
* Negócio: instabilidade do sistema e perda de confiança

**Classificação:**
Importante (alta criticidade estrutural)

---

### 4. Arquivo de 4.000 linhas

**Causa raiz provável:**

* Crescimento orgânico sem refatoração
* Falta de separação de responsabilidades
* Ausência de padrões arquiteturais

**Risco:**

* Técnico: baixa manutenibilidade
* Negócio: aumento do tempo de entrega e risco de erros

**Classificação:**
Importante

---

### 5. Ausência de testes automatizados

**Causa raiz provável:**

* Falta de cultura de testes
* Pressão por entregas rápidas
* Código difícil de testar

**Risco:**

* Técnico: regressões frequentes
* Negócio: instabilidade contínua

**Classificação:**
Importante (base de todos os problemas)

---

## Seção 2 — Plano de ação

### Prioridade 1 — Resolver duplicidade de pedidos

**Ação técnica:**

* Implementar chave única no banco (ex: idempotency_key)
* Garantir transações atômicas
* Adicionar validação antes da criação

**Esforço estimado:**
1–2 dias

**Critério de sucesso:**

* Nenhum pedido duplicado em ambiente de produção
* Testes validando criação idempotente

---

### Prioridade 2 — Melhorar performance do endpoint

**Ação técnica:**

* Adicionar índices no banco
* Implementar paginação
* Revisar queries (evitar N+1)
* Possível uso de cache

**Esforço estimado:**
2–3 dias

**Critério de sucesso:**

* Tempo de resposta < 1 segundo em carga normal
* Monitoramento mostrando redução de latência

---

### Prioridade 3 — Introduzir testes automatizados básicos

**Ação técnica:**

* Criar testes unitários para regras críticas (ex: cálculo de frete)
* Criar testes de integração para endpoints principais
* Configurar pipeline básico de CI

**Esforço estimado:**
2–4 dias

**Critério de sucesso:**

* Cobertura mínima de testes nas funcionalidades críticas
* Detecção de erros antes de deploy

---

## Seção 3 — Decisão de arquitetura

**Opção escolhida: Refatoração incremental**

**Justificativa:**

Dado o contexto:

* Sistema em produção
* Ausência de testes
* Time ocupado
* Risco alto de regressão

A reescrita completa (Opção B) apresenta risco elevado, pois não há segurança para validar comportamento correto.

A refatoração incremental permite:

* Melhorar o código gradualmente
* Introduzir testes aos poucos
* Reduzir riscos de quebra em produção

**Estratégia adotada:**

* Extrair pequenas responsabilidades em serviços menores
* Criar testes ao redor do código existente (approach "test around")
* Evoluir arquitetura progressivamente

---

## Seção 4 — Requisitos Não Funcionais ignorados

### 1. Desempenho

**Problema:**
Endpoint com tempo de resposta elevado (8–12 segundos)

**Impacto:**
Experiência do usuário comprometida e possível perda de vendas

**Métrica:**

* Tempo médio de resposta < 1s
* Percentil 95 (P95) < 2s

---

### 2. Confiabilidade

**Problema:**
Pedidos duplicados e alterações diretas em produção

**Impacto:**
Inconsistência de dados e instabilidade do sistema

**Métrica:**

* Taxa de erro < 1%
* Zero ocorrência de duplicidade

---

### 3. Manutenibilidade

**Problema:**
Código monolítico com 4.000 linhas e sem testes

**Impacto:**
Dificuldade de evolução e alto risco de regressão

**Métrica:**

* Cobertura de testes > 60% nas áreas críticas
* Redução do tamanho médio dos módulos

---

### 4. Governança e qualidade de código

**Problema:**
Deploy direto em produção sem revisão

**Impacto:**
Risco elevado de falhas

**Métrica:**

* 100% das mudanças via Pull Request
* Pipeline CI obrigatório antes de deploy

---

## Considerações finais

O sistema apresenta sinais claros de degradação técnica e ausência de práticas de engenharia fundamentais.

O plano proposto prioriza:

* Redução de riscos imediatos (duplicidade e performance)
* Introdução de qualidade (testes e processos)
* Evolução sustentável da arquitetura

A abordagem incremental permite estabilizar o sistema sem interromper a operação, criando base para melhorias contínuas.
