from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='welcome-page'),
    path('upload/', views.file_upload, name='upload-page'),
    path('waiting/', views.waiting_scan, name='waiting-page'),
    path('results/', views.results, name='result-page'),
    path('check/', views.results, name='result-page'),
]