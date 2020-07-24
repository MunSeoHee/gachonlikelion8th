from django.shortcuts import render, redirect, get_object_or_404
from .models import Sample

# Create your views here.
def index(request):
    x = Sample.objects
    return render(request, 'index.html',{'samples':x})

def new(request):
    return render(request, 'new.html')

def create(request):
    sample = Sample() # 빈 오브젝트
    sample.title = request.GET['text1']
    sample.text = request.GET['text2']
    sample.category = request.GET['text3']
    sample.save()
    return redirect('/')

def detail(request, id):
    info = get_object_or_404(Sample, pk=id)
    return render(request, 'detail.html', {'info':info})
