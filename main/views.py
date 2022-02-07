from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def login(request):
    if(request.method == 'POST'):
        user = User.objects.all()
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in user:
            if(i.email==email and i.master_password== password):
                return redirect('home')
    return render(request, 'main/login.html')

def register(request):
    if(request.method == 'POST'):
        user = User()
        user.name = request.POST.get('name')
        user.email = request.POST.get('email')
        user.master_password = request.POST.get('password')
        user.key = '1234'
        # print(name, email, master_password)
        user.save()
        return redirect('login')
    return render(request, 'main/register.html')

