using Microsoft.AspNetCore.Mvc;
using TaskManager.Api.Models;

[ApiController]
[Route("tasks")]
public class TasksController : ControllerBase
{
    private readonly TaskService _service;

    public TasksController(TaskService service)
    {
        _service = service;
    }

    [HttpGet]
public IActionResult Get(string? status = null)
    {
        return Ok(_service.GetAll(status));
    }

    [HttpPost]
    public IActionResult Create([FromBody] TaskItem task)
    {
        try
        {
            var created = _service.Create(task.Title);
            return Created($"/tasks/{created.Id}", created);
        }
        catch (Exception ex)
        {
            return BadRequest(ex.Message);
        }
    }

[HttpPatch("{id}")]
    public IActionResult Update(Guid id, [FromBody] UpdateTaskDto dto)
    {
        try
        {
            _service.Update(
                id,
                dto.Title,
                dto.Status
            );

            return NoContent();
        }
        catch
        {
            return NotFound();
        }
    }

    [HttpDelete("{id}")]
    public IActionResult Delete(Guid id)
    {
        _service.Delete(id);
        return NoContent();
    }

}