from django.shortcuts import render
from django.http import HttpResponse

import Home


# Create your views here.
#def homepage(request):   // Here we were using HTML without templa te
#   return HttpResponse("<h1> CRUD Operations </h1>")
def homepage(request):
    peoples = [
        {'name': 'Kabeer', 'age': 19},
        {'name': 'krishna', 'age': 21},
        {'name': 'Irshad', 'age': 24},
        {'name': 'Amit', 'age': 12},
        {'name': 'Gagan', 'age': 14},
    ]
    return render(request, "index.html",context={'peoples':peoples})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
