export type TaskItemStatus = "Pendente" | "Concluida";

export interface Task {
  id: string;
  title: string;
  status: TaskItemStatus;
}