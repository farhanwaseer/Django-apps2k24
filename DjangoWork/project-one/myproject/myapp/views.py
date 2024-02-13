from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.template import loader


def home(request):
    return HttpResponse("<h1> Welcome to Little Lemon! </h1>")

def farhan(request):
    return HttpResponse("<h1>Hello world! Django app created BY FARHAN WASEER")

# def drinks(request,drink_name):
#     drink = {
#         'mocha' : 'type of coffee',
#         'tea' : 'type of hot beverage',
#         'lemonade': 'type of refreshment'
#     }
#     choice_of_drink = drink[drink_name]
#     return HttpResponse(f"<h2>{drink_name}</h2> " + choice_of_drink)



def drinks(request, drink_name):
    drink = {
       'mocha' : 'type of coffee',
        'tea' : 'type of hot beverage',
        'lemonade': 'type of refreshment',
    }

    choice_of_drink = drink[drink_name]
    return HttpResponse(f'<h2>{drink_name}</h2>' + choice_of_drink)

def about(response):
    return HttpResponse('<h2>About</h2>')

def menu(response):
    return HttpResponse('<h2>Menu</h2>')

def book(response):
    return HttpResponse('<h2>Book</h2>')

def pathview(request,name,id):
    return HttpResponse(f'<h2>Name: {name}<br/> UserId: {id}</h2>')

def qryview(request):
    name = request.GET['name']
    id = request.GET['id']

    return HttpResponse(f'<h2>With qury View Name: {name} UserId: {id}</h2>')

def showform(request):
    return render(request, 'form.html')

def getform(request): 
    if request.method == "POST": 
        name=request.POST['name'] 
        id=request.POST['id'] 
    return HttpResponse(f"Name:{name} UserID:{id}") 