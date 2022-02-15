# Generated by Django 4.0.2 on 2022-02-15 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_vacancy_active_alter_candidatevacancy_last_schooling'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidatevacancy',
            options={'verbose_name': 'Candidato para Vaga', 'verbose_name_plural': 'Candidatos para Vagas'},
        ),
        migrations.AlterModelOptions(
            name='vacancy',
            options={'verbose_name': 'Vaga', 'verbose_name_plural': 'Vagas'},
        ),
        migrations.AlterField(
            model_name='candidatevacancy',
            name='salary_expectation',
            field=models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], default='Pretensão Salarial', max_length=15),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_range',
            field=models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], max_length=15, verbose_name='Faixa Salarial'),
        ),
    ]