from django.shortcuts import render
from django.http import HttpResponse
import os 

def index(request):
    TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    context = {'content': 'Good Day! This content is dynamically inserted.'}
    return render(request, 'index.html', context)
