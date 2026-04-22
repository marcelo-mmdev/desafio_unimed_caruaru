# Engenharia — Kata 2


## Arquitetura Backend

Adotei uma arquitetura em camadas:

* Controller: responsável pela interface HTTP
* Service: responsável pela lógica de negócio
* Repository: responsável pela persistência

Essa separação melhora a organização, testabilidade e manutenibilidade do código.

---

## Confiabilidade da API

Para garantir confiabilidade em produção, eu implementaria:

* Logging estruturado para rastreamento de erros
* Monitoramento com métricas (ex: tempo de resposta, taxa de erro)
* Tratamento global de exceções
* Health checks para verificação do estado da aplicação

---

## Escalabilidade

Em um cenário com múltiplos usuários e autenticação:

* Introduziria autenticação (JWT)
* Associaria tarefas a usuários
* Utilizaria banco de dados relacional (ex: PostgreSQL)
* Aplicaria cache para otimizar leitura
* Consideraria uso de filas para processamento assíncrono

---

## Observabilidade e Qualidade

Para garantir visibilidade em produção, seriam implementados:

* Logs estruturados com correlação de requisições
* Monitoramento com ferramentas como Prometheus/Grafana
* Alertas baseados em taxa de erro e latência

---

## Trade-offs adotados

Para este desafio, optei por:

* Persistência em memória, priorizando simplicidade
* Ausência de autenticação, assumindo contexto single-user

Essas decisões reduzem complexidade, mas não seriam adequadas em ambiente produtivo.

---
