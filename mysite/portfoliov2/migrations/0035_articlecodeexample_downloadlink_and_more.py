# Generated by Django 4.0.3 on 2023-09-14 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0034_alter_articlepicture_imgsrc'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecodeexample',
            name='downloadLink',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
        migrations.AddField(
            model_name='articlecodeexample',
            name='githubLink',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
