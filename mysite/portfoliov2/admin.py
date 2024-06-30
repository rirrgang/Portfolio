from django.contrib import admin
from nested_admin import NestedTabularInline, NestedModelAdmin

# Register your models here.

from . import models


@admin.register(models.ExperienceStations)
class MyModelAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.ExperienceStations._meta.get_fields()]
    ordering = ['pk']


@admin.register(models.Contact)
class MyModelAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.Contact._meta.get_fields() if field.concrete]
    ordering = ['pk']


@admin.register(models.Projects)
class MyModelAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Projects._meta.get_fields(
    ) if field.concrete and field.name != 'details']
    ordering = ['pk']


@admin.register(models.ProjectModels)
class ProjectModelsAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.ProjectModels._meta.get_fields() if field.concrete]
    ordering = ['pk']


@admin.register(models.ProjectMusic)
class ProjectModelsAdmin(admin.ModelAdmin):
    list_display = [
        field.name for field in models.ProjectMusic._meta.get_fields() if field.concrete]
    ordering = ['pk']


class PictureInline(NestedTabularInline):
    model = models.ArticlePicture
    extra = 0


class VideoInLine(NestedTabularInline):
    model = models.ArticleVideo
    extra = 0


class CodeExampleInline(NestedTabularInline):
    model = models.ArticleCodeExample
    extra = 0


class CodeLinkInline(NestedTabularInline):
    model = models.ArticleCodeLinks
    extra = 0


class ArticleInline(NestedTabularInline):
    model = models.Article
    extra = 0
    inlines = [PictureInline, VideoInLine, CodeExampleInline, CodeLinkInline]


@admin.register(models.Article)
class ArticleAdmin(NestedModelAdmin):
    list_display = [
        field.name for field in models.Article._meta.get_fields() if field.concrete]
    ordering = ['pk']
    inlines = [PictureInline, VideoInLine, CodeExampleInline, CodeLinkInline]
    show_change_link = True


@admin.register(models.ProjectProgramming)
class ProjectProgrammingAdmin(NestedModelAdmin):
    list_display = [
        field.name for field in models.ProjectProgramming._meta.get_fields() if field.concrete]
    ordering = ['pk']
    inlines = [ArticleInline]
    show_change_link = True
