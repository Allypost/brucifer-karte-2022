# Generated by Django 4.2.16 on 2024-10-20 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0072_guests_boughttickettime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='translations',
            name='value',
            field=models.CharField(blank=True, default='', max_length=500000),
        ),
    ]