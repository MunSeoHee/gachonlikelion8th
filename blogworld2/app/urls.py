from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('create/',views.create, name="create"),
    path('update/<int:pk>', views.updatePost, name="update"),
    path('delete/<int:pk>', views.deletePost, name="delete"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('covid/', views.covid, name="covid"),



]