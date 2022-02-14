# Generated by Django 4.0.2 on 2022-02-11 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vacancy',
            name='minimum_schooling',
            field=models.CharField(choices=[('Ensino Fundamental', 'ENSINO FUNDAMENTAL'), ('Ensino Médio', 'ENSINO MÉDIO'), ('Tecnólogo', 'TECNÓLOGO'), ('Ensino Superior', 'ENSINO SUPERIOR'), ('Pós/MBA/Mestrado', 'PÓS/MBA/MESTRADO'), ('Doutorado', 'DOUTORADO')], max_length=20, verbose_name='Escolaridade Mínima'),
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='salary_range',
            field=models.CharField(choices=[('Até 1000', 'ATÉ 1000'), ('De 1000 a 2000', 'DE 1000 A 2000'), ('De 2000 a 3000', 'DE 2000 A 3000'), ('Acima de 3000', 'ACIMA DE 3000')], max_length=15, verbose_name='Faixa Salarial'),
        ),
    ]