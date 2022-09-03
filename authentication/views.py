from django.shortcuts import render,redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password,check_password
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.utils import timezone
from .models import *

# Create your views here.
def home(request):
    return render(request,'authentication/index.html')
def signup(request):
    if request.method=='GET':
        return render(request,'signup.html')
    else:
        username=request.POST.get('username')
        first_name=request.POST.get('firstname')
        last_name=request.POST.get('lastname')
        email=request.POST.get('email')
        password=request.POST.get('password')
        error_message=None
        customer=Customer(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
        

        if(not username):
            error_message="Username Required"
        if(not first_name):
            error_message="First Name Required"
        if(not last_name):
            error_message="Last Name Required"
        if customer.isExists():
            error_message="Email Address Already Registered"
        if not error_message:
            customer.password=make_password(customer.password)
            customer.register()
            return redirect(signin)
        else:
            return render(request,'signup.html',{'error':error_message})
    
    
def signin(request):
    if request.method=="POST":
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
           flag=check_password(password,customer.password)
           print (password)
           print(customer.password)
           if flag:
               request.session['customer_id']=customer.id
               request.session['email']=customer.email
               request.session['username']=customer.username
               request.session['first_name']=customer.first_name
               request.session['last_name']=customer.last_name
               return redirect(second)
           else:
               error_message="Invalid EmailId or Password"
               return render(request,'signin.html',{'error':error_message})
        else:
            error_message="Invalid EmailId or Password"
            return render(request,'signin.html',{'error':error_message})
    
    return render(request,'signin.html')
def post(request):
    item=request.POST.get('item')
    remove=request.POST.get('remove')
    cart=request.session.get('cart')
    if cart:
        quantity=cart.get(item)
        if quantity:
            if remove:
                if quantity<=1:
                    cart.pop(item)
                else:
                    cart[item]=quantity-1 
            else:
                cart[item]=quantity+1
        else:
            cart[item]=1
    else:
        cart={}
        cart[item]=1
    request.session['cart']=cart
    print(cart)
    return redirect('second')

def second(request):
   cart=request.session.get('cart')
   if not cart:
       request.session.cart={}
   items=Item.get_all_items();
   print(items)
   return render(request,'second.html',{'items':items})


def search(request):
    if request.method=="GET":
        query=request.GET.get('query')
    if query:
        items=Item.objects.filter(name__icontains=query)
        return render(request,'search.html',{'items':items})
    else:
        return render(request,'search.html',{})
def profile(request):
    
    username=request.session['username']
    first_name=request.session['first_name']
    last_name=request.session['last_name']
    email=request.session['email']

    
    return render(request,'profile.html',{'email':email,'username':username,'first_name':first_name,'last_name':last_name})
def cart(request):
    try:
        ids=list(request.session.get('cart').keys())
        items=Item.get_all_items_ById(ids)
        return render(request,'cart.html',{'items':items,'cart':cart})
    except:
        return render(request,'empty.html')

def signout(request):
    logout(request)
    messages.success(request,"You are logged out Successfully")
    return render(request,'authentication/index.html')