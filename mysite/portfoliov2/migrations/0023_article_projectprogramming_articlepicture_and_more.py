# Generated by Django 4.0.3 on 2023-06-27 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfoliov2', '0022_remove_articlecodeexample_article_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('isVisible', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectProgramming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authors', models.TextField(blank=True, default='')),
                ('project', models.ForeignKey(limit_choices_to={'category': 'Programming'}, on_delete=django.db.models.deletion.CASCADE, to='portfoliov2.projects')),
            ],
        ),
        migrations.CreateModel(
            name='ArticlePicture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imgSrc', models.FilePathField(blank=True, path='portfoliov2/static/portfoliov2/pictures/', recursive=True)),
                ('caption', models.CharField(max_length=200)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfoliov2.article')),
            ],
        ),
        migrations.CreateModel(
            name='ArticleCodeExample',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.TextField()),
                ('language', models.CharField(max_length=50)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfoliov2.article')),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='project',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portfoliov2.projectprogramming'),
        ),
    ]