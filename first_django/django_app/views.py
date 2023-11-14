from django.shortcuts import render
from django.http import HttpResponse
from .models import AccessRecord
import os 

def index(request):
    TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
    context = {'content': 'Good Day! This content is dynamically inserted.'}
    return render(request, 'index.html', context)

def second_page(request):
    return render(request, 'second_page.html')

def access_records(request):
    records = AccessRecord.objects.all()
    print(len(records))  # this line for debugging
    
    return render(request, 'index.html', {'records': records})

