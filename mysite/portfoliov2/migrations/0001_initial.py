# Generated by Django 4.2.1 on 2023-06-14 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExperienceStations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('fa-solid fa-graduation-cap', 'Education'), ('fa-solid fa-briefcase', 'Experience')], max_length=100)),
                ('title', models.CharField(max_length=100)),
                ('station', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('date', models.DateTimeField()),
            ],
        ),
    ]