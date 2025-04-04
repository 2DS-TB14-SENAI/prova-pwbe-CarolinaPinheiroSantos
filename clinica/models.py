from django.db import models

class Medico(models.Model):
    nome = models.CharField(max_length=30)
    escolhas = [
    ("CAR", "cardiologista" ),
    ("ORT", "ortopedista"),
    ("GIN", "ginecologista")]
    especialidade = models.CharField(max_length=3, choices=escolhas)
    crm = models.CharField(max_length=30)
    email = models.EmailField(null=True)

    def __str__(self):
        return self.nome
    
class Consulta(models.Model):
    paciente = models.CharField(max_length=30)
    data = models.DateTimeField()
    medico =  models.ForeignKey(Medico, on_delete=models.CASCADE)
    escolhas_status = [
    ("agendado", "agendado" ),
    ("realizado", "realizado"),
    ("cancelado", "cancelado")]
    status = models.CharField(max_length=15, choices=escolhas_status)

    def __str__(self):
        return self.paciente