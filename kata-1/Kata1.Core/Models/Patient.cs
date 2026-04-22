namespace Kata1.Core.Models;

public enum UrgencyLevel
{
    Baixa = 1,
    Media = 2,
    Alta = 3,
    Critica = 4
}

public class Patient
{
    public string Name { get; set; }
    public int Age { get; set; }
    public UrgencyLevel Urgency { get; set; }
    public DateTime ArrivalTime { get; set; }
}