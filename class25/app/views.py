from django.shortcuts import render, get_object_or_404,redirect
from .models import list
import datetime
# Create your views here.
def index(request):
    arr = list.objects
    #x = get_object_or_404(list, pk=1)
    return render(request, 'index.html',{"arr":arr})

def new(request):
    return render(request, 'new.html')

def create(request):
    ob = list()
    ob.price = request.GET["price"]
    ob.num = request.GET["num"]
    ob.product = request.GET["product"]
    if request.GET.get("check") == 'on':
        ob.check = True
    else:
        ob.check =False
    ob.save()
    return redirect('/')

def detail(request, id):
    ob = get_object_or_404(list, pk=id)
    return render(request, "detail.html",{"x":ob})

def update(request, id):
    ob = get_object_or_404(list, pk=id)
    return render(request, "update.html",{"x":ob})

def updat(request,id):
    ob = get_object_or_404(list, pk=id)
    ob.price = request.GET['price']
    ob.num = request.GET['num']
    ob.product = request.GET['product']
    if request.GET.get("check") == 'on':
        ob.check = True
    else:
        ob.check =False
    ob.save()
    ob.date = datetime.datetime.now()
    

    return redirect('/'+str(id))

def delete(request, id):
    ob = get_object_or_404(list, pk=id)
    ob.delete()
    return redirect('/')