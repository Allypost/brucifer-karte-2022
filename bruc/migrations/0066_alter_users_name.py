# Generated by Django 4.0.4 on 2024-02-07 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0065_alter_users_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='name',
            field=models.CharField(blank=True, default='', max_length=50),
        ),
    ]
