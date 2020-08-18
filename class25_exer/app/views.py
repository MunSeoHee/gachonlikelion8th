from django.shortcuts import render, get_object_or_404,redirect
from .models import List
import datetime

# Create your views here.
def index(request):
    arr = List.objects
    return render(request,'index.html',{'arr':arr})

def new(request):
    return render(request, 'new.html')

def create(request):
    ob = List()
    ob.price = request.GET["price"]
    ob.num = request.GET["num"]
    ob.product = request.GET["product"]
    if request.GET.get("check") == 'on':
        ob.check = True
    else:
        ob.check = False
    ob.save()
    return redirect('/')

def detail(request, id):
    ob = get_object_or_404(List, pk=id)
    return render(request, "detail.html",{'x':ob})

def udate(request, id):
    ob = get_object_or_404(List, pk=id)
    return render(request, "update.html", {"x":ob})
