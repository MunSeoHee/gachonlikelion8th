from django.http import HttpResponse
from django.shortcuts import redirect

# 로그인 된 상태로 모르고 다시 로그인 하려고 할떄 기본 페이지로 돌아가게 하는 함수 만들기
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        else: # 로그인 되어 있지 않다면 view에 해당하는 함수 실행
            return view_func(request, *args, **kwargs)
    return wrapper_func

# 관리자만 접속가능한 기능 추가
def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse('이 페이지에 대한 권한없습니다.')
        return wrapper_func
    return decorator

def admin_only(view_func):
	def wrapper_function(request, *args, **kwargs):
		group = None
		if request.user.groups.exists():
			group = request.user.groups.all()[0].name

		if group == 'customer':
			return redirect('user')

		if group == 'admin':
			return view_func(request, *args, **kwargs)

	return wrapper_function