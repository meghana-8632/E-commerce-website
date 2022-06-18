from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Items

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method=="POST":
        username=request.POST.get('username')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        
        if User.objects.filter(username=username).first():
            messages.error(request,"the username is already taken ")
            messages.success(request,"Your Account has been successfully created")
            return redirect('signin')
            
        else:
            new_user=User.objects.create_user(username,email,pass1)
            new_user.first_name=fname
            new_user.last_name=lname
            new_user.save()
            messages.success(request,"Your Account has been successfully created")
            return redirect('signin')
    return render(request,'signup.html')
    
    
def signin(request):
    if request.method=="POST":
        username=request.POST.get('username')
        pass1=request.POST.get('pass1')
        user=authenticate(username=username, password=pass1)
        if user is not None:
            login(request,user)
            fname=user.first_name
            return redirect('second')
        
        else:
            messages.error(request,"Bad Credentials")
            return redirect('home')
    
    return render(request,'signin.html')
def second(request):
    items=Items.objects.all()
    return render(request,'second.html',{'items':items})
def search(request):
    if request.method=="GET":
        query=request.GET.get('query')
    if query:
        items=Items.objects.filter(name__icontains=query)
        return render(request,'search.html',{'items':items})
    else:
        return render(request,'search.html',{})
def profile(request):
    
    return render(request,'profile.html',{'user':request.user})

        
def signout(request):
    logout(request)
    messages.success(request,"You are logged out Successfully")
    return render(request,'authentication/index.html')