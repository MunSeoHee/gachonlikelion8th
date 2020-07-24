"""user URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path #view.py를 import해오기

from firstapp import views

urlpatterns = [
    path('', views.index, name='index'), #''=rootURL, views.index=views의 index 메서드의 결과로 나오는 페이지, 
    path('admin/', admin.site.urls),
] #''인 URL에 접속하면 views에서 정의되어 있는 index라는  함수의 결과를 웹페이지에 띄운다. 

urlpatterns = [
      path('firstapp', include('firstapp.urls')), #app내 urls.py로 역할 이동시키기
      path('second',include('second.urls')),
      path('admin/', admin.site.urls),
  ]
