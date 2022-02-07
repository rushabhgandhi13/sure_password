from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import *

# Create your views here.
def home(request):
    return render(request, 'main/index.html')

def service(request,pk):
    cur_user= User.objects.get(id=pk)
    service = Service.objects.filter(user = cur_user)
    context={
        'service' : service,
    }
    if(request.method == 'POST'):
        user = Service()
        user.service_name = request.POST.get('name')
        user.user = cur_user
        user.password = request.POST.get('password')
        user.save()

    return render(request, 'main/service.html', context)

def login(request):
    user_id=1
    if(request.method == 'POST'):
        user = User.objects.all()
        email = request.POST.get('email')
        password = request.POST.get('password')
        for i in user:
            if(i.email==email and i.master_password== password):
                user_id = i.id
                return redirect('service', pk=user_id)
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

def delete(request, pk):
    query = Service.objects.get(id=pk)
    cur_user1 = User.objects.get(id= query.user.id)
    uid = cur_user1.id
    query.delete()
    return redirect('service', pk=uid)