from django.shortcuts import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'django_welcome.html')
