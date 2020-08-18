from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm,CreateUserForm

from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, admin_only
from django.contrib.auth.models import Group

from .filters import OrderFilter
#from django.contrib.auth import login

   
# Create your views here.
@login_required(login_url = 'login')
@admin_only
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context ={'orders':orders, 'customers':customers,
    'total_customers:':total_customers,'delivered':delivered,
    'pending':pending} 
    
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def customer(request,pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    order_count = orders.count()

    myFilter = OrderFilter(request.GET, queryset=orders)
    orders = myFilter.qs

    context ={'customer':customer,'orders':orders,
    'order_count':order_count,'myFilter':myFilter}
    
    return render(request, 'accounts/customer.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def products(request):
    products = Product.objects.all()
    return render(request, 'accounts/products.html',{'products':products})

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def createOrder(request):
	form = OrderForm()
	if request.method == 'POST':
		#print('Printing POST:', request.POST)
		form = OrderForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')

	context= {'form':form}
	return render(request, 'accounts/order_form.html',context)

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def updateOrder(request,pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)

    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')

@login_required(login_url = 'login')
@allowed_users(allowed_roles=['admin'])
def deleteOrder(request, pk):
    order  = Order.objects.get(id=pk)
    if request.method == "POST":
        order.delete()
        return redirect('/')
    context = {'item':order}
    return render(request, 'accounts/delete.html',context)

@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, '계정생성완료 ' + user)

            return redirect('login')
    
    context = {'form':form}
    return render(request, 'accounts/register.html',context)

@unauthenticated_user
def loginPage(request):
	# if request.user.is_authenticated:
	# 	return redirect('home')
	# else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')

			user = authenticate(request, username=username, password=password)  

			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request,'아이디 혹은 비밀번호가 잘못입력되었습니다!')
		context  = {}
		return render(request, 'accounts/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(allowed_roles=['customer'])
def userPage(request):
    orders = request.user.customer.order_set.all()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    print('주문',orders)
    context = {'orders':orders, 'total_orders':total_orders,
    'delvered':delivered, 'pending':pending}
    return render(request, 'accounts/user.html',context)

