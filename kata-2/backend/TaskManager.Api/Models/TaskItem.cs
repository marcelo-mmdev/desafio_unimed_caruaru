
using System.Text.Json.Serialization;

namespace TaskManager.Api.Models;

public enum TaskItemStatus
{
    Pendente,
    Concluida
}

public class TaskItem
{
    public Guid Id { get; set; } = Guid.NewGuid();
    public string Title { get; set; } = string.Empty;
    public TaskItemStatus Status { get; set; } = TaskItemStatus.Pendente;
}

public class UpdateTaskDto
{
    [JsonPropertyName("title")]
    public string? Title { get; set; }
    
[JsonPropertyName("status")]
    public string? Status { get; set; }


}
