from django.shortcuts import render, redirect, get_object_or_404
from .models import Blog
import datetime

# Create your views here.
def index(request):
    blog = Blog.objects
    return render(request, 'index.html',{'blogs':blog})

def create(request):
    return render(request, 'create.html')

def new(request):
    blog = Blog()
    blog.title =request.GET['title']
    blog.title =request.GET['body']
    blog.title =request.GET['like']
    blog.save()
    return redirect('/')

def detail(request, blog_id):
    blog= get_object_or_404(Blog,pk=blog_id)
    return render(request, 'detail.html',{{'blog':blog}})

def update(request, blog_id):
    blog= get_object_or_404(Blog,pk=blog_id)
    return render(request, 'update.html',{{'blog':blog}})

def updat(request, blog_id): # 수정 후 화면 이동 
    blog= get_object_or_404(Blog,pk=blog_id)
    blog.title = request.GET['title']
    blog.body = request.GET['body']
    blog.like = request.GET['like']
    blog.date = request.datetime.now()
    blog.save()
    return redirect('/detail/'+str(blog_id)) # 문자형변환 (문자 + 문자(문자로 변환된 숫자)

def delete(request, blog_id):
    blog= get_object_or_404(Blog,pk=blog_id)
    blog.delete()
    return redirect('/')