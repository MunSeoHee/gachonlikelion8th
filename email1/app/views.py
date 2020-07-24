from django.shortcuts import render, get_object_or_404, redirect
from .models import Email
from django.utils import timezone

# Create your views here.
def home(request):
    emails = Email.objects
    return render(request, 'home.html', {'emails':emails})

def detail(request):
    email_detail = get_object_or_404(Email, pk=email_id)
    return render(request, 'detail.html', {'email':email_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    email = Email()
    email.address = request.GET['address']
    email.pub_date = timezone.datetime.now()
    email.title = request.GET['title']
    email.content = request.GET['content']
    email.save()
    return redirect('/email/'+str(email.id))

def edit(request, email_id):
    email =get_object_or_404(Email, pk=email_id)
    return render(request, 'edit.html', {'email':email})

def update(request,email_id):
    email = get_object_or_404(Email, pk=email_id)
    email.address = request.GET['address']
    email.pub_date = timezone.datetime.now()
    email.title = request.GET['title']
    email.content = request.GET['content']
    email.save()
    return redirect('/email/' + str(email.id))

def delete(request, email_id):
    email = get_object_or_404(Email, pk=email_id)
    email.delete()
    return redirect('home')


    