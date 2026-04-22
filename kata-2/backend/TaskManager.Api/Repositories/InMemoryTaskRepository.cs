using TaskManager.Api.Models;

public class InMemoryTaskRepository : ITaskRepository
{
    private readonly List<TaskItem> _tasks = new();

    public List<TaskItem> GetAll() => _tasks;

    public TaskItem? GetById(Guid id) =>
        _tasks.FirstOrDefault(t => t.Id == id);

    public void Add(TaskItem task) => _tasks.Add(task);

    public void Update(TaskItem task)
    {
        var existing = GetById(task.Id);
        if (existing == null) return;

        existing.Title = task.Title;
        existing.Status = task.Status;
    }

    public void Delete(Guid id)
    {
        var task = GetById(id);
        if (task != null) _tasks.Remove(task);
    }
}