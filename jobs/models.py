from django.db import models
from django.contrib.auth import get_user_model


SALARY_CHOICES = (
    (1000, 'Até 1000'),
    (2000, 'De 1000 a 2000'),
    (3000, 'De 2000 a 3000'),
    (9999, 'Acima de 3000' ),
)

SCHOOLING_CHOICES = (
    (1, 'Ensino Fundamental'),
    (2, 'Ensio Médio'),
    (3, 'Tecnólogo'),
    (4, 'Ensino Superior'),
    (5, 'Pós/MBA/Mestrado'),
    (6, 'Doutorado'),
)

class Vacancy(models.Model):
    name = models.CharField('Nome da Vaga', max_length=200)
    salary_range = models.IntegerField('Faixa Salarial', choices=SALARY_CHOICES)
    requirements = models.TextField('Requisitos', max_length=1000)
    minimum_schooling = models.IntegerField('Escolaridade Mínima', choices=SCHOOLING_CHOICES)
    active = models.BooleanField('Vaga Disponivel?', default=True)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = ('Vaga')
        verbose_name_plural = ('Vagas')

class CandidateVacancy(models.Model):
    vacancy = models.ForeignKey(Vacancy, verbose_name='Vaga', on_delete=models.CASCADE)
    candidate = models.ForeignKey(get_user_model(), verbose_name='Candidato', on_delete=models.CASCADE)
    salary_expectation = models.IntegerField(default='Pretensão Salarial', choices=SALARY_CHOICES)
    experience = models.TextField('Experiência', max_length=400)
    last_schooling = models.IntegerField('Última Escolaridade', choices=SCHOOLING_CHOICES)

    def __str__(self):
        return f'{self.candidate.first_name} {self.candidate.last_name} - {self.vacancy.name}'


    class Meta:
        verbose_name = ('Candidato para Vaga')
        verbose_name_plural = ('Candidatos para Vagas')