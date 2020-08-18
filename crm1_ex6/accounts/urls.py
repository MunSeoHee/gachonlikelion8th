from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products,name="products"),
    path('customer/<str:pk_test>/', views.customer,name="customer"),
    path('create_order/', views.createOrder, name="create_order"),
    path('update/<str:pk>', views.updateOrder, name="update"),
    path('delete/<str:pk>', views.deleteOrder, name="delete"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user"),
    

]