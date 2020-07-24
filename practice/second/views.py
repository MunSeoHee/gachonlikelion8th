from django.shortcuts import render
from django.http import HttpResponseRedirect

from second.models import Post
from .forms import PostForm



def list(request):
    context = {
        'items': Post.objects.all()
    }
    return render(request, 'second/list.html', context)

def create(request): # form 이라는 instance를 만들어 'creat.html'으로 보냄
    if request.method == 'POST':
         form = PostForm(request.POST)
         if form.is_valid():
             new_item = form.save()
         return HttpResponseRedirect('/second/list/')
    form = PostForm()
        return render(request, 'second/create.html', {'form':form})

def confirm(request):
    form = PostForm(request.POST)  # request의 POST 데이터들을 바로 PostForm에 담을 수 있습니다.
    if form.is_valid(): # 데이터가 form 클래스에서 정의한 조건 (max_length 등)을 만족하는지 체크합니다.
        return render(request, 'second/confirm.html', {'form': form}) # 부합하는 데이터면 form data를 confirm template에 넘격주고 렌더링
    return HttpResponseRedirect('/create/')  # 데이터가 유효하지 않으면 되돌아갑니다.