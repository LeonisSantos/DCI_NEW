# Generated by Django 4.2.4 on 2023-08-11 13:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dci', '0010_otsdci_proprietario'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='otsdci',
            name='num_ots',
        ),
        migrations.RemoveField(
            model_name='otsdci',
            name='ots_id',
        ),
        migrations.RemoveField(
            model_name='otsdci',
            name='sigla',
        ),
    ]