# Generated by Django 4.2.7 on 2023-12-11 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_socios', '0004_jugador_imagen_perfil'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('equipo_local', models.CharField(max_length=100)),
                ('equipo_visitante', models.CharField(max_length=100)),
                ('fecha', models.DateField()),
            ],
        ),
    ]
