# Generated by Django 4.2.1 on 2023-06-14 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='experiencestations',
            name='date',
        ),
        migrations.AddField(
            model_name='experiencestations',
            name='date_from',
            field=models.DateField(default='2023-01-01'),
        ),
        migrations.AddField(
            model_name='experiencestations',
            name='date_to',
            field=models.DateField(default='2023-01-01'),
        ),
    ]
