using Kata1.Core.Models;
using Kata1.Core.Services;

namespace Kata1.Tests;

public class TriageServiceTests
{
    private readonly TriageService _service = new();

    [Fact]
    public void Elderly_With_Medium_Should_Become_High()
    {
        var patients = new List<Patient>
        {
            new Patient
            {
                Name = "Idoso",
                Age = 65,
                Urgency = UrgencyLevel.Media,
                ArrivalTime = DateTime.Now
            },
            new Patient
            {
                Name = "Adulto",
                Age = 30,
                Urgency = UrgencyLevel.Media,
                ArrivalTime = DateTime.Now.AddMinutes(-10)
            }
        };

        var result = _service.OrderQueue(patients);

        Assert.Equal("Idoso", result.First().Name);
    }

    [Fact]
    public void Minor_Should_Increase_Priority()
    {
        var patients = new List<Patient>
        {
            new Patient
            {
                Name = "Menor",
                Age = 15,
                Urgency = UrgencyLevel.Baixa,
                ArrivalTime = DateTime.Now
            },
            new Patient
            {
                Name = "Adulto",
                Age = 30,
                Urgency = UrgencyLevel.Baixa,
                ArrivalTime = DateTime.Now.AddMinutes(-5)
            }
        };

        var result = _service.OrderQueue(patients);

        Assert.Equal("Menor", result.First().Name);
    }

    [Fact]
    public void Same_Priority_Should_Order_By_Arrival()
    {
        var patients = new List<Patient>
        {
            new Patient
            {
                Name = "Paciente1",
                Age = 30,
                Urgency = UrgencyLevel.Alta,
                ArrivalTime = DateTime.Now
            },
            new Patient
            {
                Name = "Paciente2",
                Age = 30,
                Urgency = UrgencyLevel.Alta,
                ArrivalTime = DateTime.Now.AddMinutes(-10)
            }
        };

        var result = _service.OrderQueue(patients);

        Assert.Equal("Paciente2", result.First().Name);
    }
}