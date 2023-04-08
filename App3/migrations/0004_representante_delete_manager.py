# Generated by Django 4.1.7 on 2023-04-08 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App3', '0003_equipo_jugadores'),
    ]

    operations = [
        migrations.CreateModel(
            name='Representante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('sitio_web', models.URLField()),
                ('contrato_total', models.BooleanField()),
            ],
        ),
        migrations.DeleteModel(
            name='Manager',
        ),
    ]
