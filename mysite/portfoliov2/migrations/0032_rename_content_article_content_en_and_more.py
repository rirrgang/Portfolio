# Generated by Django 4.0.3 on 2023-09-13 15:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0031_rename_title_projects_title_en_projects_title_de'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='content',
            new_name='content_en',
        ),
        migrations.RenameField(
            model_name='article',
            old_name='title',
            new_name='title_en',
        ),
    ]
