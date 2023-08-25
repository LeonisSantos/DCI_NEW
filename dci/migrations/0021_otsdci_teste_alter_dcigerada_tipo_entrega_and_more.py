# Generated by Django 4.2.4 on 2023-08-18 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dci', '0020_alter_dcigerada_link_alter_dcigerada_obv_atr_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='otsdci',
            name='teste',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='dcigerada',
            name='tipo_entrega',
            field=models.CharField(choices=[('TOTAL', 'Total'), ('PARCIAL', ' Parcial'), ('FINAL', 'Final')], default='', max_length=150),
        ),
        migrations.AlterField(
            model_name='otsdci',
            name='proprietario',
            field=models.CharField(default='', max_length=100, null=True),
        ),
    ]
