using TaskManager.Api.Models;

public interface ITaskRepository
{
    List<TaskItem> GetAll();
    TaskItem? GetById(Guid id);
    void Add(TaskItem task);
    void Update(TaskItem task);
    void Delete(Guid id);
}