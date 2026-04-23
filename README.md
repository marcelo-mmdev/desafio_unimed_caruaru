# Teste de Seleção — Desenvolvimento

**Nome:** Manoel Marcelo Rodrigues
**Telefone:** (81) 98904-4977
**E-mail:** [marcelo.mmdev@gmail.com](mailto:marcelo.mmdev@gmail.com)

---

## 📌 Visão Geral

Este repositório contém a implementação dos quatro katas propostos no teste técnico, abordando diferentes aspectos do desenvolvimento de software, incluindo lógica, desenvolvimento full-stack, análise de engenharia e processamento de dados.

O objetivo principal foi priorizar **clareza de raciocínio, organização do código e tomada de decisões técnicas bem fundamentadas**, conforme orientado no desafio.

---

## 🧰 Stack Utilizada

* **Backend:** C# com .NET 8
* **Frontend:** React + TypeScript
* **Dados:** Python (pandas)

### Justificativa

Optei por utilizar a stack sugerida no desafio (C#/.NET, React e Python) com o objetivo de manter aderência ao ambiente tecnológico da equipe e facilitar a avaliação comparativa.

No backend, o **.NET** foi escolhido pela sua robustez, tipagem forte e maturidade na construção de APIs REST.

No frontend, utilizei **React com TypeScript** visando maior segurança de tipos, melhor organização e facilidade de manutenção.

Para o pipeline de dados, utilizei **Python com pandas**, pela alta produtividade na manipulação, limpeza e transformação de dados.

---

## ▶️ Como Executar o Projeto

### Pré-requisitos

* .NET 8 SDK
* Node.js (v18 ou superior)
* Python 3.10+

---

### 🧩 Kata 1 — Fila de Triagem

Implementação da lógica de priorização de pacientes.

```bash
cd kata-1
dotnet test
```

---

### 🧩 Kata 2 — Painel de Tarefas

#### Backend

```bash
cd kata-2/backend/TaskManager.Api
dotnet run

```md
Para testar a aplicação:

1. Acesse o frontend
2. Crie uma tarefa
3. Marque como concluída
4. Utilize os filtros

A aplicação consome a API em tempo real.
```

A API estará disponível em:
http://localhost:5222

---

#### Frontend

```bash
cd kata-2/frontend/TaskManager
npm install
npm run dev
```

O Front-end estará disponível em:
http://localhost:5173

---

### 🧩 Kata 3 — Análise de Engenharia

O plano técnico pode ser encontrado em:

```
kata-3/PLANO.md
```

---

### 🧩 Kata 4 — Pipeline de Dados

#### Pré-requisito

```bash
pip install pandas

cd kata-4/src
python pipeline.py

kata-4/output/consolidado.csv
```


---

## ⚙️ Decisões Técnicas

* Estruturei o backend utilizando separação em camadas (**Controller, Service e Repository**) para garantir organização e manutenibilidade.
* Optei por soluções simples e diretas, priorizando clareza e legibilidade em vez de otimizações prematuras.
* Utilizei persistência simplificada (em memória ou SQLite) no Kata 2, considerando o escopo do desafio.
* Implementei validações básicas e tratamento de erros para garantir consistência da aplicação.
* No pipeline de dados, priorizei legibilidade e reprodutibilidade das transformações.

---

## ⚖️ Trade-offs Considerados

* A escolha por persistência simples reduz complexidade inicial, mas não atende cenários de produção com alta concorrência ou necessidade de durabilidade.
* A ausência de autenticação no Kata 2 foi uma decisão consciente para manter foco no escopo principal da feature.
* No processamento de dados, a utilização de pandas atende bem volumes moderados, mas pode não escalar para grandes volumes sem adaptações.

---

## 🚀 Melhorias Futuras

Se tivesse mais tempo, eu:

* Implementaria autenticação e controle de usuários no Kata 2
* Adicionaria testes automatizados mais abrangentes (unitários e de integração)
* Utilizaria Docker para padronizar o ambiente de execução
* Melhoraria a observabilidade com logs estruturados e métrricas
* Evoluiria o pipeline de dados para suportar grandes volumes (ex: processamento distribuído com Spark)
* Implementaria validações mais robustas e tratamento de edge cases adicionais

---

## 📂 Estrutura do Repositório

```
/ (raiz)
  README.md
  /kata-1/
    src/
    tests/
    ANALISE.md
  /kata-2/
    backend/
    frontend/
    REQUISITOS.md
    ENGENHARIA.md
  /kata-3/
    PLANO.md
  /kata-4/
    data/
      pedidos.csv
      clientes.csv
      entregas.csv
    src/
      pipeline.py
    output/
      consolidado.csv
      indicadores.json
    ANALISE.md
```

---

## ⭐ Diferenciais do Projeto

* Separação clara de camadas no backend (Controller, Service, Repository)
* Pipeline de dados resiliente a inconsistências reais
* Tratamento de erros e validações básicas implementadas
* Código organizado e legível, com foco em manutenção
* Documentação clara e orientada ao avaliador

---

## 🧠 Considerações Finais

Busquei abordar cada kata não apenas com foco na implementação, mas também na **qualidade das decisões técnicas, clareza na comunicação e organização do pensamento**, aspectos fundamentais no desenvolvimento de software em ambientes reais.

---
