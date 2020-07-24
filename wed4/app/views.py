from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.
def home(request):
    blogs = Blog.objects # 객체 묶음 가져오기
    return render(request, 'home.html', {'blogs':blogs})
    # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blogs 객체도 함께 넘겨주도록 하겠다.

def detail(request, blog_id) : 
    blog_detail = get_object_or_404(Blog, pk= blog_id) # 특정 객체 가져오기(없으면 404 에러)
    return render(request, 'detail.html', {'blog':blog_detail})
    # render라는 함수를 통해 페이지를 띄워줄 건데, home.html 파일을 띄워줄 것이고 
    # 이 때, blog 객체도 함께 넘겨주도록 하겠다.


