# Generated by Django 4.2.4 on 2023-08-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dci', '0003_dcionline_lista_teste'),
    ]

    operations = [
        migrations.CreateModel(
            name='OesDci',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oe_id', models.CharField(max_length=100)),
                ('num_oe', models.CharField(max_length=100)),
                ('tipo_oe', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=100)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
    ]
