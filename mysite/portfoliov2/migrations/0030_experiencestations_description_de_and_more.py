# Generated by Django 4.0.3 on 2023-09-13 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0029_rename_description_experiencestations_description_en_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='experiencestations',
            name='description_de',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='experiencestations',
            name='station_de',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='experiencestations',
            name='title_de',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='experiencestations',
            name='description_en',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='experiencestations',
            name='station_en',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='experiencestations',
            name='title_en',
            field=models.CharField(default='', max_length=100),
        ),
    ]
