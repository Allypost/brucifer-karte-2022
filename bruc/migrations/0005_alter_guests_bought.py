# Generated by Django 4.0.4 on 2022-05-09 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0004_remove_guests_id_alter_guests_jmbag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='guests',
            name='bought',
            field=models.CharField(blank=True, default='0', max_length=50),
        ),
    ]
