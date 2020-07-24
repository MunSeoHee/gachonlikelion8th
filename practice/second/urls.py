#second/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list, name='list'),
    path('create/', views.create, name='create'), # 추가 
    path('confirm/', views.confirm, name='confirm'),
]