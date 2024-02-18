from django.urls import path

from . import views

app_name='myapp'

urlpatterns = [
    path('', views.home, name='home'),
    path('farhan/', views.farhan, name='farhan'),
    path('about/', views.about, name='about'),
    path('menu/', views.menu, name='menu'),
    path('book/', views.book, name='book'),
    # path('drinks/', views.drinks, name='drinks'),
    path('drinks/<str:drink_name>',views.drinks,name='drink_name'),
    path('getuser/<name>/<id>', views.pathview, name='pathview'),
    path('myapp/getuser/', views.qryview, name='qryview'),
    path('myapp/showform/', views.showform, name='showform'),
    path("myapp/getform/", views.getform, name='getform'),    
]