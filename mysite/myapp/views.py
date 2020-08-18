from django.shortcuts import render, redirect
from .models import user,board
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.utils import timezone
# Create your views here.

def index(request):
    return render(request, 'temp/index.html')

def regist(request):
    return render(request, 'temp/regist.html')

def sign_up(request):
    if request.method == "POST":
        name = request.POST.get("id")
        passwd = request.POST.get("pw")
        user_info = user()
        user_info.name = name
        user_info.passwd = make_password(passwd)
        user_info.save()
    return redirect('/')

def home(request):
    
    user_id = request.session.get('user1')
    message={}
   
    if user_id :
        message = str(user.objects.get(name=user_id)) +" 님 반갑습니다" #key 로써 name 을 사용하면 char 형식을 받는다.
        return render(request,'temp/main1.html',{'message':message})   # 로그인을 했다면, username 출력

    return check_session(request)

def sign_in(request):
    response_data = {}

    if request.method == "POST":
        login_username = request.POST.get('id', None)
        login_password = request.POST.get('pw', None)
        if not (login_username and login_password):
            response_data['error']="뭔가 입력이 안되었네요."
        else : 
            try:
                user1 = user.objects.get(name=login_username) 
            except:
                response_data['error']='그런 아이디는 없는데요?'
                return render(request, 'temp/login.html',response_data)
            user1 = user.objects.get(name=login_username) 
            if check_password(login_password, user1.passwd):
                request.session['user1'] = user1.name 
                #세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                #세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('/home')
            else:
                response_data['error'] = "그런 비밀번호는 없는데요?"

        return render(request, 'temp/login.html',response_data)

def logout(request):
    request.session.pop('user1')
    return redirect('/')

def make_board(request):
    user_id = request.session.get('user1')
    message={}
    if user_id :
        return render(request,'temp/createboard.html')

    return check_session(request)

def check_session(request):
    response_data = {}
    response_data['error'] = "로그인 왜안함?"
    return render(request, 'temp/login.html',response_data)

def create_board(request):
    user_id = request.session.get('user1')
    if not user_id :
        return check_session(request)

    board1 = board()
    board1.name = request.POST.get('name', None)
    board1.date = timezone.datetime.now()
    board1.memo = request.POST.get('memo', None)
    board1.save()
    return render(request,'temp/main1.html')

def myboard(request):
    user_id = request.session.get('user1')
    message={}
    board1 = board.objects
    board_list = board.objects.all()
    paginator = Paginator(board_list,3)
    page = request.GET.get('page', None)
    posts = paginator.get_page(page)
    if user_id :        
        return render(request,'temp/myboard.html',{'board':board1, 'post':posts})   # 로그인을 했다면, username 출력

    return check_session(request)

def delete_board(request):
    board1 = board.objects.get(date=request.GET['date'])
    board1.delete()
    return redirect('/myboard')