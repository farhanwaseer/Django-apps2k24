from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('farhan/', views.farhan, name='farhan'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    # path('drinks/', views.drinks, name='drinks'),
    path('drinks/<str:drink_name>',views.drinks,name='drink_name'),    
]