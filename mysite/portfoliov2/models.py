from datetime import datetime
import os
from django.db import models
from django.core.files.storage import FileSystemStorage
from django.conf import settings


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.name


class ExperienceStations(models.Model):
    expTypes = [
        ("fa-solid fa-graduation-cap", "Education"),
        ("fa-solid fa-briefcase", "Experience"),
    ]
    type = models.CharField(
        max_length=100,
        choices=expTypes,
    )
    title_en = models.CharField(max_length=100, default='')
    title_de = models.CharField(max_length=100, default='')
    station_en = models.CharField(max_length=100, default='')
    station_de = models.CharField(max_length=100, default='')
    description_en = models.TextField(default='')
    description_de = models.TextField(default='')
    date_from = models.DateField(default='2023-01-01')
    date_to = models.DateField(default='2023-01-01')


class Projects(models.Model):
    id = models.AutoField(primary_key=True)
    title_en = models.CharField(max_length=100)
    title_de = models.CharField(max_length=100, default='')
    categories = [
        ("Programming", "Programming"),
        ("3D Modelling", "3D Modelling"),
        ("Music", "Music"),
        ("Video", "Video"),
    ]
    category = models.CharField(max_length=100, choices=categories)
    categorieSymbols = [
        ("fa-solid fa-code", "Programming"),
        ("fa-solid fa-cube", "3D Modelling"),
        ("fa-solid fa-music", "Music"),
        ("fa-solid fa-video", "Video"),
    ]
    categorySymbol = models.CharField(
        max_length=100, choices=categorieSymbols, default="", blank=True)
    createdOn = models.DateTimeField(auto_now_add=True)
    editedOn = models.DateTimeField(auto_now=True)
    isVisible = models.BooleanField(default=True)
    description_en = models.TextField(default='', blank=True)
    description_de = models.TextField(default='', blank=True)
    details_en = models.TextField(default='', blank=True)
    details_de = models.TextField(default='', blank=True)
    imgSrc = models.TextField(default='', blank=True)

    def __str__(self):
        return self.title_en

    class Meta:
        ordering = ['category']


class ProjectModels(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, limit_choices_to={
                                'category': '3D Modelling'})
    modelSrc = models.CharField(max_length=100, default='', blank=True)


class ProjectMusic(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, limit_choices_to={
                                'category': 'Music'})
    musicSrc = models.CharField(max_length=100, default='', blank=True)
    interpreter = models.CharField(max_length=100, default='', blank=True)
    genre = models.CharField(max_length=100, default='', blank=True)

# ======================= PROJECT PROGRAMMING ======================= #


class ProjectProgramming(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE, limit_choices_to={
                                'category': 'Programming'})
    authors = models.TextField(default='', blank=True)


class Article(models.Model):
    projectProgramming = models.ForeignKey(
        ProjectProgramming, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=200)
    title_de = models.CharField(max_length=200, default='', blank=True)
    content_en = models.TextField(default='', blank=True)
    content_de = models.TextField(default='', blank=True)
    isVisible = models.BooleanField(default=True)


class ArticlePicture(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    imgSrc = models.TextField(default='', blank=True)
    caption = models.CharField(max_length=200, default='', blank=True)


class ArticleVideo(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    caption = models.CharField(max_length=200, default='', blank=True)
    videoSrc = models.TextField(default='', blank=True)


class ArticleCodeExample(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    code = models.TextField(default='', blank=True)
    language = models.CharField(max_length=50, default='', blank=True)


class ArticleCodeLinks(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    downloadLink = models.TextField(default='', blank=True)
    githubLink = models.TextField(default='', blank=True)
