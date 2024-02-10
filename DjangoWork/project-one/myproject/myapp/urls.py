from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farhan/', views.farhan, name='farhan'),
    path('drinks/', views.drinks, name='drinks'),
    path('drinks/<str:drink_name>', views.drinks, name='drink_name'),
]