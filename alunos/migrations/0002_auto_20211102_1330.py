# Generated by Django 3.2.5 on 2021-11-02 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alunos', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Aluno',
        ),
        migrations.DeleteModel(
            name='Curso',
        ),
    ]
