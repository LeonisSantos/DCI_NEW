# Generated by Django 4.2.4 on 2023-08-11 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dci', '0009_remove_otsdci_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='otsdci',
            name='proprietario',
            field=models.CharField(default='', max_length=100),
        ),
    ]
