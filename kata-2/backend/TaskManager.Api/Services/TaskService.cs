using TaskManager.Api.Models;

public class TaskService
{
    private readonly ITaskRepository _repository;

    public TaskService(ITaskRepository repository)
    {
        _repository = repository;
    }

public List<TaskItem> GetAll(string? status)

    {
        var tasks = _repository.GetAll();

        if (string.IsNullOrEmpty(status))
            return tasks;

        return tasks.Where(t => t.Status.ToString().ToLower() == status.ToLower()).ToList();
    }

    public TaskItem Create(string title)
    {
        if (string.IsNullOrWhiteSpace(title))
            throw new ArgumentException("Title is required");

        var task = new TaskItem { Title = title };
        _repository.Add(task);
        return task;
    }

    public void Update(Guid id, string? title, string? status)
    {
        var task = _repository.GetById(id);
        if (task == null)
            throw new Exception("Task not found");

        if (!string.IsNullOrWhiteSpace(title))
            task.Title = title;

        if (!string.IsNullOrWhiteSpace(status))
        {
            if (Enum.TryParse<TaskItemStatus>(status, true, out var parsedStatus))
            {
                task.Status = parsedStatus;
            }
            else
            {
                throw new Exception("Invalid status");
            }
        }

        _repository.Update(task);
    }

    public void Delete(Guid id)
    {
        _repository.Delete(id);
    }
}