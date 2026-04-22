using Kata1.Core.Models;

namespace Kata1.Core.Services;

public class TriageService
{
    public List<Patient> OrderQueue(List<Patient> patients)
    {
        return patients
            .Select(p => new
            {
                Patient = p,
                Priority = CalculatePriority(p)
            })
            .OrderByDescending(x => x.Priority)
            .ThenBy(x => x.Patient.ArrivalTime)
            .Select(x => x.Patient)
            .ToList();
    }

    private int CalculatePriority(Patient patient)
    {
        int priority = (int)patient.Urgency;

        // Regra 4: Idoso com média vira alta
        if (patient.Age >= 60 && patient.Urgency == UrgencyLevel.Media)
        {
            priority = (int)UrgencyLevel.Alta;
        }

        // Regra 5: Menor ganha +1 nível
        if (patient.Age < 18)
        {
            priority += 1;
        }

        // Garantir que não ultrapasse crítica
        return Math.Min(priority, (int)UrgencyLevel.Critica);
    }
}