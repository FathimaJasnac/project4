from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def login(request):
    if request.method== 'POST':
        uname=request.POST['username']
        pswd=request.POST['password']
        user=auth.authenticate(username=uname,password=pswd)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid registration")
            return redirect('login')
    return render(request,"login.html")
def reg(request):
    if request.method== 'POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpswd = request.POST['confirm password']
        if password==cpswd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('reg')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email Taken")
                return redirect('reg')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                return redirect('login')

        else:
           messages.info(request,"password not matching")
           return redirect('reg')
        return redirect('/')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')