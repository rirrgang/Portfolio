# Generated by Django 4.0.3 on 2023-06-16 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0002_remove_experiencestations_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
