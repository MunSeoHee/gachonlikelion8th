from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def products(request):
    products = Product.objects.all()

    return render(request, 'accounts/products.html',{'products':products})