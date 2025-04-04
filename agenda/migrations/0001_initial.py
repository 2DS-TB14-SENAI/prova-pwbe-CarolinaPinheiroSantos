# Generated by Django 5.1.6 on 2025-04-04 19:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Servico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('duracao', models.PositiveIntegerField()),
                ('preco', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
        migrations.CreateModel(
            name='Agendamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_hora', models.DateTimeField()),
                ('cliente_nome', models.CharField(max_length=100)),
                ('cliente_email', models.EmailField(max_length=254)),
                ('servico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agenda.servico')),
            ],
        ),
    ]
