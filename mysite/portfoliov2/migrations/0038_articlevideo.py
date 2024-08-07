# Generated by Django 4.0.3 on 2023-09-14 16:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0037_articlecodelinks'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(blank=True, default='', max_length=200)),
                ('videoSrc', models.TextField(blank=True, default='')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfoliov2.article')),
            ],
        ),
    ]
