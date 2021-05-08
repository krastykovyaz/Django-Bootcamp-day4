from django.shortcuts import render
from django.http import HttpResponse

def framework_web(request):
    return render(request, 'ex01/django.html')

def show_static_page(request):
    return render(request, 'ex01/style.html')

def template_engine(request):
    return render(request, 'ex01/templates.html')
