import { useCallback, useEffect, useState } from "react";
import type { Task } from "./types/task";
import {
  getTasks,
  createTask,
  updateTask,
  deleteTask,
} from "./services/api";

function App() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [title, setTitle] = useState("");
  const [filter, setFilter] = useState<string>("");
  const [loading, setLoading] = useState(false);

  // 🔄 Carregar tarefas
  const loadTasks = useCallback(async () => {
    setLoading(true);
    try {
      const data = await getTasks(filter);
      setTasks(data);
    } catch {
      alert("Erro ao carregar tarefas");
    } finally {
      setLoading(false);
    }
  }, [filter]);

  useEffect(() => {
    // eslint-disable-next-line react-hooks/set-state-in-effect
    loadTasks();
  }, [loadTasks]);

  // ➕ Criar tarefa
  async function handleCreate() {
    if (!title.trim()) return;

    try {
      await createTask(title);
      setTitle("");
      loadTasks();
    } catch {
      alert("Erro ao criar tarefa");
    }
  }

  // ✅ Alternar status (checkbox)
  async function handleToggle(task: Task) {
    const newStatus = task.status === "Pendente" ? "Concluida" : "Pendente";
    
    // Optimistic update
    setTasks(prev => prev.map(t => 
      t.id === task.id ? { ...t, status: newStatus } : t
    ));

    try {
await updateTask(task.id, { title: task.title, status: newStatus });
      setFilter("");
      loadTasks();
    } catch {
      loadTasks();
      alert("Erro ao atualizar tarefa");
    }

  }

  // ❌ Deletar tarefa
  async function handleDelete(id: string) {
    try {
      await deleteTask(id);
      loadTasks();
    } catch {
      alert("Erro ao deletar tarefa");
    }
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Task Manager</h1>

      {/* Criar tarefa */}
      <div>
        <input
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          placeholder="Nova tarefa"
        />
        <button onClick={handleCreate}>Criar</button>
      </div>

      {/* Filtro */}
      <div style={{ marginTop: 10 }}>
        <button onClick={() => setFilter("")}>Todas</button>
        <button onClick={() => setFilter("Pendente")}>Pendentes</button>
        <button onClick={() => setFilter("Concluida")}>Concluídas</button>
      </div>

      {/* Loading */}
      {loading && <p>Carregando...</p>}

      {/* Lista */}
      <ul style={{ marginTop: 20 }}>
        {tasks.map((task) => (
          <li key={task.id} style={{ marginBottom: 10 }}>
            
            {/* Checkbox */}
            <input
              type="checkbox"
              checked={task.status === "Concluida"}
              onChange={() => handleToggle(task)}
              style={{ marginRight: 10 }}
            />

            {/* Título */}
            <span
              style={{
                textDecoration:
                  task.status === "Concluida" ? "line-through" : "none",
                marginRight: 10,
              }}
            >
              {task.title}
            </span>

            {/* Status visual */}
            <span style={{ marginRight: 10 }}>
              {task.status === "Concluida" ? "✅ Concluída" : "⏳ Pendente"}
            </span>

            {/* Ações */}
            <button onClick={() => handleToggle(task)}>
              {task.status === "Pendente" ? "Concluir" : "Reabrir"}
            </button>

            <button onClick={() => handleDelete(task.id)}>Excluir</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;