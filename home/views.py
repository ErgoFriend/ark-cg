from django.shortcuts import render
from django.http.response import HttpResponse

def index(request):
    return render(request, 'home/circle_hp.html')

def works(request):
    return render(request, 'home/circle_works.html')

def contact(request):
    return render(request, 'home/circle_contact.html')

def about_us(request):
    return render(request, 'home/circle_about_us.html')
