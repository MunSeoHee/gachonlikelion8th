from django.shortcuts import render, get_object_or_404,redirect
from .models import Blog
from django.utils import timezone

# Create your views here.

def home(request):
    blogs = Blog.objects # 객체 묶음 가져오기
    return render(request, 'home.html', {'blogs':blogs})
    # render라는 함수를 통해 페이지를 띄울건데,home.html파일을 띄울것
    # 이때. blogs 객체도 함께 넘겨주도록 하겠다.

def detail(request):
    blog_detail = get_object_or_404(Blog, pk=blog_id) # 특정 개체 가져오기 or 없으면 404에러
    return render(request, 'detail.html', {'blog':blog_detail})
    # render라는 함수를 이용해서 페이지를 띄울건데, blog.html 파일을 띄울것
    # 이 때 ,blogs 객체도 함께 넘겨주도록 하겠다.

def new(request):
    return render(request, 'new.html')

def create(request):
    blog = Blog() # 객체틀 하나 가져오기
    blog.title = request.GET['title'] # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 객체 저장하기 

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

# U - 기존 글을 수정할 수 있는 페이지 띄어주기
def edit(request,blog_id):
    blog = get_object_or_404(Blog, pk= blog_id) # 특정 개체 가져오기 or 없으면 404에러
    return render(request, 'edit.html', {'blog':blog})

def update(request,blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.title = request.GET['title'] # 내용 채우기
    blog.body = request.GET['body'] # 내용 채우기
    blog.pub_date = timezone.datetime.now() # 내용 채우기
    blog.save() # 저장하기

    # 새로운 글 url 주소로 이동
    return redirect('/blog/' + str(blog.id))

    # D - delete(기존 글 객체 가져와서 삭제)
def delete(request, blog_id):
    blog= get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    blog.delete()
    return redirect('home') # home 이름의 url 로

