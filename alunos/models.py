from django.db import models

class Aluno(models.Model):
    id = id = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=100)
    rg = models.CharField(max_length=9)
    cpf = models.CharField(max_length=11)
    data_nascimento = models.DateField()

    def __str__(self):
        return self.nome