from django.shortcuts import render
from .models import Procurement

def index(request):
    return render(request, 'catalog/catalog.html')
