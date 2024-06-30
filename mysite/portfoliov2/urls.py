from django.urls import path
from portfoliov2 import views

app_name = 'portfoliov2'

urlpatterns = [
    path('', views.basev2, name='base'),
    path('portfoliov2', views.basev2, name='base'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('projects', views.projects, name='projects'),
    path('projects/modelDetail/<int:pk>',
         views.modelDetail, name='modelDetail'),
    path('projects/musicDetail/<int:pk>',
         views.musicDetail, name='musicDetail'),
    path('projects/programmingDetail/<int:pk>',
         views.programmingDetail, name='programmingDetail'),
    path('contact', views.contact, name='contact'),
    path('contact/success', views.contactSuccess, name="success"),
    path('legalnotice', views.legalnotice, name="legalnotice"),
    path('switchLanguage', views.switchLanguage, name="switchLanguage"),
]
