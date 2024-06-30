from django.urls import path
from onePageTemplate import views

app_name = 'onePageTemplate'

urlpatterns = [
    path('base', views.base, name='base'),
    path('janFitzner', views.janFitzner, name='janFitzner'),
    path('tinker', views.tinker, name='tinker'),
    path('opt_legalnotice', views.legalnotice, name="legalnotice"),
]
