from doctest import master
from django.contrib import messages
from email import message
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def service(request,pk):
    cur_user= User.objects.get(id=pk)
    service = Service.objects.filter(user = cur_user)
    context={
        'service' : service,
    }
    if(request.method == 'POST' and request.POST.get('checker')=="add_service"):
        service = Service()
        service.service_name = request.POST.get('name')
        service.user = cur_user
        service.password = encrypt_password(cur_user.key,request.POST.get('password')).decode()
        service.save()
    if(request.method == 'POST' and request.POST.get('checker')=="update_service"):
        Service.objects.filter(id = request.POST.get('id')).update(service_name=request.POST.get('name'),password = encrypt_password(cur_user.key,request.POST.get('password')).decode())
    if(request.method == 'POST' and request.POST.get('checker')=="delete_user"):
        query = User.objects.get(id=cur_user.id)
        if(request.POST.get('password')==decrypt_password(cur_user.key,cur_user.master_password)):
            query.delete()
            return redirect('login')
        else:
            messages.success(request, 'Wrong password')
    return render(request, 'main/service.html', context)

def login(request):
    user_id=1
    if(request.method == 'POST'):
        user = User.objects.all()
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in user:
            # print(i.key.encode(),i.master_password.endcode())
            if(i.email==email and decrypt_password(i.key,i.master_password)== password):
                user_id = i.id
                return redirect('service', pk=user_id)
    return render(request, 'main/login.html')

def register(request):
    if(request.method == 'POST'):
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.key = Fernet.generate_key()
        master_pass = request.POST.get('password')
        user.master_password=encrypt_password(user.key,master_pass).decode()
        user.key=user.key.decode()
        # print(name, email, master_password)
        user.save()
        return redirect('login')
    return render(request, 'main/register.html')

def view_password(request,pk):
    s=Service.objects.get(id=pk)
    u=s.user.key
    temp=decrypt_password(u,s.password)
    context={
        'name': s.service_name,
        'password': temp
    }
    return render(request,'main/view_service.html', context)
def delete(request, pk):
    query = Service.objects.get(id=pk)
    cur_user1 = User.objects.get(id= query.user.id)
    uid = cur_user1.id
    query.delete()
    return redirect('service', pk=uid)


def encrypt_password(key, password):
    f = Fernet(key)
    token = f.encrypt(password.encode())
    return token


def decrypt_password(key, encrypted_password):
    f = Fernet(key)
    password = f.decrypt(encrypted_password.encode())
    return password.decode()
