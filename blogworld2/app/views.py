from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .models import *
from .forms import CreateForm,CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,logout,login
from django.contrib.auth.decorators import login_required

import requests
from xml.dom import minidom
from xml.dom.minidom import Node


def covid(request):
    api_key = "hu52sTh3n%2FVfgNDnXWZ%2FbO7GJnWth5EWloJPowEnFfIhxw8v%2BfMe2D9erS4shyGoz1FjwGnbsEDkW4cIPS9ygQ%3D%3D"
    api_key_decode = requests.utils.unquote(api_key) 
    parameters = {
        "ServiceKey":api_key_decode,
        "numOfROws":1, "pageNo":1,
        "startCreateDt":20200806,
        "endCreateDt":20200807} 
    req = requests.get("http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19InfStateJson?", params = parameters)
    xmlraw = minidom.parseString(req.text)
    clist= xmlraw.getElementsByTagName('item')
    tree = clist[0].toxml()
    for node in clist:
        alist = node.getElementsByTagName('decideCnt')
       
        for a in alist:
            title = a.firstChild.data
            #message = str(title)
            #print("확진자 수 " ,message)
            print("확진자 수 " ,title)
    context = {'title':title}
    #context = {'message':message}
    return render(request, 'app/covid.html',context)

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, "계정생성완료 " + user)

                return redirect('login')
        context = {'form':form}
        return render(request, 'app/register.html',context)

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username , password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, '입력오류')
        return render(request, 'app/login.html')
    
def logoutUser(request):
	logout(request)
	return redirect('login')

@login_required(login_url='login')
def home(request):
    blogs = Blog.objects.all()

    context = {'blogs':blogs}
    return render(request, 'app/home.html',context)

@login_required(login_url='login')
def create(request):
    form = CreateForm()
    if request.method == 'POST':
        form = CreateForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'form':form}
    return render(request, 'app/create.html',context)

@login_required(login_url='login')
def updatePost(request, pk):
    blogs = Blog.objects.get(id=pk)
    form = CreateForm(instance=blogs)

    if request.method == 'POST':
        form = CreateForm(request.POST, instance=blogs)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form':form}
    return render(request, 'app/create.html',context)

@login_required(login_url='login')
def deletePost(request, pk):
    blogs = Blog.objects.get(id=pk)
    if request.method == "POST":
        blogs.delete()
        return redirect('/')

    context = {'item':blogs}
    return render(request, 'app/delete.html',context)