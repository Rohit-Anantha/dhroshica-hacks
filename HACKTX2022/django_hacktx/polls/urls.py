from django.urls import path

from . import views

urlpatterns = [
    path('polls/', views.index, name ='index'),
    path('urmom/', views.urmom, name='urmom')
]

