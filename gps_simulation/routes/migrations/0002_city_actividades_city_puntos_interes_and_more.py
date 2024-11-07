# Generated by Django 5.1.1 on 2024-11-07 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='actividades',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='puntos_interes',
            field=models.TextField(default='Sin información'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='city',
            name='turismo_info',
            field=models.TextField(blank=True, null=True),
        ),
    ]
