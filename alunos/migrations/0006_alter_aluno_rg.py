# Generated by Django 3.2.5 on 2021-11-03 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0005_alter_aluno_nome'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aluno',
            name='rg',
            field=models.CharField(max_length=10),
        ),
    ]
