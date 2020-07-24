#firstapp/urls.py
from django.urls import path
 
  from . import views
  
urlpatterns = [
    path('', views.index, name='index'),
     path('select/', views.select, name='select'),
     path('result/', views.result, name='result'),
] # 일일이 url mapping 시켜줘야함

urlpatterns = [
     path('', views.index, name='index'),
     path('select/<int:number>/', views.select, name='select'),
     path('result/', views.result, name='result'),
 ] # 변수화 사용 <int:number>