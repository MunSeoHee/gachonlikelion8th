# from django.http import HttpResponse
# 이제 HttpResponse 말고 shortcut인 render을 써보자
from django.shortcuts import render
from .models import Question


def index(request):
  # question 인스턴스들을 불러오는 코드
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'latest_question_list': latest_question_list})