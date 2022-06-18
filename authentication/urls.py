from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('' ,views.home,name="home"),
    path('signup' ,views.signup,name="signup"),
    path('signin' ,views.signin,name="signin"),
    path('second' ,views.second,name="second"),
    path('signout' ,views.signout,name="signout"),
    path('search',views.search,name="search"),
    path('profile',views.profile,name="profile"),
    
]