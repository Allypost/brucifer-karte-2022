# Generated by Django 4.0.4 on 2022-09-25 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bruc', '0032_mailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='mailer',
            name='mai',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='mailer',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]