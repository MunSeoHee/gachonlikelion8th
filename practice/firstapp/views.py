#firstapp/views.py

from django.shortcuts import render
#from django.http import HttpResponse
#from django.template import loader
from datetime import datetime #시간 정보를 받기 위해 datetime import

def index(request): #index라는 함수는 request를 받아서 HttpResponse를 return 한다.
    #template = loader.get_template('firstapp/index.html') # index.html을 가져와서 template라는 변수에 저장
    now = datetime.now() # now라는 변수에 datetime.now()의 리턴값 받기
    context = {
        'current_date': now
    }# 데이터->template꾸며주기
    #return HttpResponse("Hello world.") # Http응답 : template이란 변수 렌더링
    return render(request, 'firstapp/index.html', context) # 주석된 두 줄 코드를 render함수로 간단히 표현, 순서(request, template,context)

def select(request): # 변수화 사용x
      message = '수 하나를 입력해주세요.'
      context={'number':4}
      return HttpResponse(message)

def select(request, number): # 변수화 사용o
      message = '수 하나를 입력해주세요.'
      context={'number':4}
      return HttpResponse(message)

def result(request):
      message = '추첨 결과입니다.'
      context={'number':[1,2,3,4,5,6]}
      return render(request, 'firstapp/index.html',context)
  
 