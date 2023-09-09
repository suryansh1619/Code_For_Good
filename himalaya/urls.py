
from django.contrib import admin
from django.urls import path,include
from . import views

app_name="himalaya"

urlpatterns = [
    path('home/', views.homepage ,name="home"),
    path('home/authuser', views.authuser , name="login_signup"),
    path('home/login', views.loginuser , name="login"),
    path('home/signup', views.signup , name="signup"),
    path('home/tourism', views.tourismmain , name="tourism"),
    path('home/tourism/bilaspur', views.bilaspur , name="bilaspur"),
    path('home/tourism/chamba', views.chamba , name="chamba"),
    path('home/tourism/hamirpur', views.hamirpur , name="hamirpur"),
    path('home/tourism/kangra', views.kangra , name="kangra"),
    path('home/tourism/kinnaur', views.kinnaur , name="kinnaur"),
    path('home/tourism/kullu', views.kullu , name="kullu"),
    path('home/tourism/una', views.una , name="una"),
    path('home/tourism/mandi', views.mandi , name="mandi"),
    path('home/tourism/shimla', views.shimla , name="shimla"),
    path('home/tourism/lahual_spiti', views.lahual_spiti, name="lahual&spiti"),
    path('home/tourism/gettripplan', views.gettripplan , name="gettripplan"),
    path('home/tourism/tripplan', views.tripplanner , name="displaytripplan"),
    path('home/tourism/getweatherdata', views.getweatherdata , name="getweatherdata"),
    path('home/tourism/displayweatherdata', views.weatherdata, name="displayweather")
]