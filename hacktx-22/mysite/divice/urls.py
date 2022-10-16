from django.urls import path

from . import views

urlpatterns = [
    path('', views.welcome, name='default-welcome-page'),
    path('home/', views.welcome, name='welcome-page'),
    path('upload/', views.upload_image, name='upload-page'),
    path('waiting/', views.waiting_scan, name='waiting-page'),
    path('check/', views.check_scan, name='check-page'),
    path('people/', views.input_names, name='people-page'),
    path('assign/', views.assign_items, name='assign-page'),
    path('calculating/', views.waiting_calc, name='calculate-page'),
    path('results/', views.results, name='result-page'),
    # these next ones are for form stuffies
    path('payee-name/', views.payee_name, name='payee-form-receiver'),

]