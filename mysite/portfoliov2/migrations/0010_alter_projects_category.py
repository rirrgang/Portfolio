# Generated by Django 4.0.3 on 2023-06-17 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0009_alter_projects_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projects',
            name='category',
            field=models.CharField(choices=[(1, 'Programming'), (2, '3D Modelling'), (3, 'Music'), (4, 'Video')], max_length=100),
        ),
    ]
