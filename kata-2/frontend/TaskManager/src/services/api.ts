import type { Task } from "../types/task";

const BASE_URL = "http://localhost:5222/tasks";

export async function getTasks(status?: string): Promise<Task[]> {
  const url = status ? `${BASE_URL}?status=${status}` : BASE_URL;

  const res = await fetch(url);
  return res.json();
}

export async function createTask(title: string): Promise<Task> {
  const res = await fetch(BASE_URL, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ title }),
  });

  return res.json();
}

export async function updateTask(id: string, updates: Partial<Task>) {
  await fetch(`${BASE_URL}/${id}`, {
    method: "PATCH",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(updates),
  });
}

export async function deleteTask(id: string) {
  await fetch(`${BASE_URL}/${id}`, {
    method: "DELETE",
  });
}