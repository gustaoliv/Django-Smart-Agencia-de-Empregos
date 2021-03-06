# Generated by Django 4.0.2 on 2022-02-21 22:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('name', models.CharField(max_length=200, verbose_name='Nome da Vaga')),
                ('salary_range', models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], verbose_name='Faixa Salarial')),
                ('requirements', models.TextField(max_length=1000, verbose_name='Requisitos')),
                ('minimum_schooling', models.IntegerField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Tecnólogo'), (4, 'Ensino Superior'), (5, 'Pós/MBA/Mestrado'), (6, 'Doutorado')], verbose_name='Escolaridade Mínima')),
                ('active', models.BooleanField(default=True, verbose_name='Vaga Disponivel?')),
            ],
            options={
                'verbose_name': 'Vaga',
                'verbose_name_plural': 'Vagas',
            },
        ),
        migrations.CreateModel(
            name='CandidateVacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criado', models.DateField(auto_now_add=True, verbose_name='Data de Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Data de atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('salary_expectation', models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], default='Pretensão Salarial')),
                ('experience', models.TextField(max_length=400, verbose_name='Experiência')),
                ('last_schooling', models.IntegerField(choices=[(1, 'Ensino Fundamental'), (2, 'Ensino Médio'), (3, 'Tecnólogo'), (4, 'Ensino Superior'), (5, 'Pós/MBA/Mestrado'), (6, 'Doutorado')], verbose_name='Última Escolaridade')),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Candidato')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='jobs.vacancy', verbose_name='Vaga')),
            ],
            options={
                'verbose_name': 'Candidato para Vaga',
                'verbose_name_plural': 'Candidatos para Vagas',
            },
        ),
    ]
