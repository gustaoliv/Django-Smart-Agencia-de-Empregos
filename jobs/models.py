from django.db import models


class Vacancy(models.Model):
    SALARY_CHOICES = (
        ('ATÉ 1000', 'ATÉ 1000'),
        ('DE 1000 A 2000', 'DE 1000 A 2000'),
        ('DE 2000 A 3000', 'DE 2000 A 3000'),
        ('ACIMA DE 3000', 'ACIMA DE 3000'),
    )
    SCHOOLING_CHOICES = (
        ('ENSINO FUNDAMENTAL', 'ENSINO FUNDAMENTAL'),
        ('ENSINO MÉDIO', 'ENSINO MÉDIO'),
        ('TECNÓLOGO', 'TECNÓLOGO'),
        ('ENSINO SUPERIOR', 'ENSINO SUPERIOR'),
        ('PÓS/MBA/MESTRADO', 'PÓS/MBA/MESTRADO'),
        ('DOUTORADO', 'DOUTORADO'),
    )

    name = models.CharField('Nome da Vaga', max_length=200)
    salary_range = models.CharField('Faixa Salarial', max_length=15, choices=SALARY_CHOICES)
    requirements = models.TextField('Requisitos', max_length=400)
    minimum_schooling = models.CharField('Escolaridade Mínima', max_length=20, choices=SCHOOLING_CHOICES)

    def __str__(self):
        return self.name