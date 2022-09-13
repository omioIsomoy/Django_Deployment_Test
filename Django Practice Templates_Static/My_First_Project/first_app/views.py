from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home(request):
    dic={'text_1':'Hello'}
    return render(request, 'first_app/index.html', context=dic)
def contact(request):
    return HttpResponse("<h1>This is contact page.</h1> <a href='/'>Home</a> <a href='/about/'>About</a>")
def about(request):
    return HttpResponse("<h1>This is about page.</h1> <a href='/contact/'>Contact</a> <a href='/'>Home</a>")
