# Análise de Requisitos — Kata 2

## Ambiguidades identificadas

### 1. Definição de status da tarefa

**Ambiguidade:**
Não está claro como a situação da tarefa deve ser representada.

**Pergunta ao cliente:**
A tarefa deve ter apenas dois estados (pendente/concluída) ou múltiplos estados (ex: em andamento, cancelada)?

**Decisão adotada:**
Implementei dois estados: `Pendente` e `Concluída`, por simplicidade e aderência ao requisito mínimo.

---

### 2. Edição de tarefas

**Ambiguidade:**
Não foi especificado se tarefas podem ser editadas após criação.

**Pergunta ao cliente:**
O usuário pode alterar o título ou outras propriedades da tarefa?

**Decisão adotada:**
Permiti atualização parcial via endpoint `PATCH`, incluindo título e status.

---

### 3. Identificação de usuário

**Ambiguidade:**
Não há definição de usuários no sistema.

**Pergunta ao cliente:**
As tarefas são individuais por usuário ou compartilhadas?

**Decisão adotada:**
Considerei um sistema single-user (sem autenticação), onde todas as tarefas pertencem ao mesmo contexto.

---

### 4. Ordenação das tarefas

Ambiguidade:
Não está definido se as tarefas devem seguir alguma ordenação específica.

Pergunta ao cliente:
As tarefas devem ser ordenadas por data de criação, prioridade ou status?

Decisão adotada:
Mantive a ordem de criação (FIFO), por simplicidade.

---

## Requisitos Funcionais (RF)

* RF01: O sistema deve permitir criar uma tarefa com título
* RF02: O sistema deve listar todas as tarefas
* RF03: O sistema deve permitir filtrar tarefas por status
* RF04: O sistema deve permitir atualizar o status da tarefa
* RF05: O sistema deve permitir remover tarefas

---

## Requisitos Não Funcionais (RNF)

* RNF01: A API deve responder em formato JSON
* RNF02: O sistema deve possuir tempo de resposta inferior a 500ms em operações simples
* RNF03: O código deve ser organizado e de fácil manutenção
* RNF04: O sistema deve ser resiliente a entradas inválidas
* RNF05: A aplicação deve ser executável localmente sem dependências complexas

---

## Backlog — Prioridade

O requisito de prioridade foi considerado como melhoria futura.

Foi incluído no backlog como:

* Implementar campo de prioridade (baixa, média, alta)
* Permitir ordenação por prioridade
* Atualizar interface para exibição visual da prioridade

Essa abordagem segue o princípio de entregar primeiro o núcleo funcional e evoluir incrementalmente.
