from django.shortcuts import render, redirect, get_object_or_404
from .models import User
import datetime

# Create your views here.
def user(request):
    user = User.objects
    return render(request, 'user.html',{'users':user})

def create(request):
    return render(request, 'create.html')

def new(request):
    user = User()
    user.email =request.GET['email']
    user.pw =request.GET['pw']
    user.name =request.GET['name']
    if request.GET.get('gender') == '1':
        user.gender = True
    else :
        user.gender = False
    user.age =request.GET['age']
    user.save()
    return redirect('/user')


def detail(request, user_id):
    user= get_object_or_404(User,pk=user_id)
    return render(request, 'detail.html',{{'user':user}})

def update(request, user_id):
    user= get_object_or_404(Blog,pk=user_id)
    return render(request, 'update.html',{{'user':user}})

def updat(request, user_id): # 수정 후 화면 이동 
    user= get_object_or_404(User,pk=user_id)
    user.email = request.GET['email']
    user.pw = request.GET['pw']
    user.name = request.GET['name']
    user.gender = request.GET['gender'] # 추후에 if-else 문써서 수정할것!
    user.age = request.GET['age']
    user.date = request.datetime.now()
    user.save()
    return redirect('/detail/'+str(user_id)) # 문자형변환 (문자 + 문자(문자로 변환된 숫자)

def delete(request, user_id):
     user= get_object_or_404(User,pk=user_id)
     user.delete()
     return redirect('/user')