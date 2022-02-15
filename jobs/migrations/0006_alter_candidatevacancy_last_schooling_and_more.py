# Generated by Django 4.0.2 on 2022-02-15 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0005_alter_candidatevacancy_options_alter_vacancy_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidatevacancy',
            name='last_schooling',
            field=models.IntegerField(choices=[(1, 'ENSINO FUNDAMENTAL'), (2, 'ENSINO MÉDIO'), (3, 'TECNÓLOGO'), (4, 'ENSINO SUPERIOR'), (5, 'PÓS/MBA/MESTRADO'), (6, 'DOUTORADO')], verbose_name='Última Escolaridade'),
        ),
        migrations.AlterField(
            model_name='candidatevacancy',
            name='salary_expectation',
            field=models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], default='Pretensão Salarial'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='minimum_schooling',
            field=models.IntegerField(choices=[(1, 'ENSINO FUNDAMENTAL'), (2, 'ENSINO MÉDIO'), (3, 'TECNÓLOGO'), (4, 'ENSINO SUPERIOR'), (5, 'PÓS/MBA/MESTRADO'), (6, 'DOUTORADO')], verbose_name='Escolaridade Mínima'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_range',
            field=models.IntegerField(choices=[(1000, 'Até 1000'), (2000, 'De 1000 a 2000'), (3000, 'De 2000 a 3000'), (9999, 'Acima de 3000')], verbose_name='Faixa Salarial'),
        ),
    ]