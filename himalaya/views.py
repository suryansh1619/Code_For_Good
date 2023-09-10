
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from datetime import timedelta
import json
import urllib.request
import urllib.parse
import openai
# Create your views here.

user=forecast=None
errormsg1=errormsg2=tripplan=''

def homepage(request):
    return render(request,'himalaya/home.html',context={"user":user})

def tourismmain(request):
    if user!=None and user.is_authenticated:
        return render(request,"himalaya/tour.html",context={})
    return HttpResponseRedirect(reverse('himalaya:login_signup'))

def authuser(request):
    return render(request,'himalaya/login.html',context={"error_msg1":errormsg1,"error_msg2":errormsg2,})

def loginuser(request):
    global user,errormsg1
    username=request.POST['username']
    pwd=request.POST['password']
    print(username,pwd,user)
    user=authenticate(request,username=username,password=pwd)
    print(username,pwd,user)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse('himalaya:home'))
    else:
        print("Login Insuccessful")
        errormsg1='Invalid Credentials'
        return HttpResponseRedirect(reverse('himalaya:login_signup'))    
    
def signup(request):
    global user,errormsg2
    uname=request.POST["name"]
    email=request.POST["email_id"]
    pwd=request.POST["passwd"]
    print(uname,email,pwd)
    try:
        tempuser = User.objects.create_user(uname,email,pwd)
        tempuser.first_name=uname
        user=tempuser
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("himalaya:home")) 
    except:
        errormsg2="User name already exists"
        return HttpResponseRedirect(reverse("himalaya:login_signup"))

def getweatherdata(request):
    global forecast
    
    date=request.POST["date"]
    place=request.POST["place"]+",HP,INDIA"
    print(date,place)
    BaseURL = 'https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/'

    ApiKey='SHLY7RWBEGPDMNY4R3T66QUX4'
    UnitGroup='us'
    
    Apiquery=BaseURL+place+"/"+date+"?"+"&unitGroup"+UnitGroup+"&key="+ApiKey
    try:
        req=urllib.request.urlopen(Apiquery)
    except:
        print("Not able to get data")
        return HttpResponseRedirect(reverse("himalaya:weather"))
    
    rawdata=req.read()
    req.close()
    forecast=json.loads(rawdata)
    
    return HttpResponseRedirect(reverse("himalaya:displayweather"))


def weatherdata(request):
    global forecast
    if user!=None and user.is_authenticated:
        
    
        currdate=timezone.now().strftime("%Y-%m-%d")
        maxdate=(timezone.now()+timedelta(days=15)).strftime("%Y-%m-%d")
        temp=days=None
        if forecast is not None:
            temp=forecast
            days=forecast['days'][0]
            forecast=None
        return render(request,"himalaya/weather.html",context={"forecast":temp,
                                                                "days":days,
                                                                "today":currdate,
                                                                "maxdate":maxdate,})
    else:
        return HttpResponseRedirect(reverse('himalaya:login_signup'))
    
def tripplanner(request):
    global tripplan
    if user!=None and user.is_authenticated:
        temp=None
        startdate=timezone.now().strftime("%Y-%m-%d")
        enddate=(timezone.now()+timedelta(120)).strftime("%Y-%m-%d")
        if tripplan!='':
            temp=tripplan
            tripplan=''
        return render(request,"himalaya/tripdetails.html",context={
            "tripplan":temp,
            "startdate":startdate,
            "enddate":enddate,
        })
    else:
        return HttpResponseRedirect(reverse('himalaya:login_signup'))
    
def gettripplan(request):
    global tripplan
    
    openai.api_key = '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'
    messages = [ {"role": "system", "content": 
                "You are a intelligent assistant."} ]
    date=request.POST['date']
    enddate=request.POST['enddate']
    place=request.POST['place']+',HP'
    print(date,enddate,place)
    message = "Create an iteniary for visiting "+place+" from "+date+" to "+enddate
    if message:
        messages.append(
            {"role": "user", "content": message},
        )
        chat = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )
    reply = chat.choices[0].message.content
    tripplan= reply
    messages.append({"role": "assistant", "content": reply})
    return HttpResponseRedirect(reverse('himalaya:displaytripplan'))

def bilaspur(request):
    return render(request,"himalaya/bilaspur.html",context={})
def chamba(request):
    return render(request,"himalaya/chamba.html",context={})
def hamirpur(request):
    return render(request,"himalaya/hamirpur.html",context={})
def kangra(request):
    return render(request,"himalaya/kangra.html",context={})
def kinnaur(request):
    return render(request,"himalaya/kinnaur.html",context={})
def una(request):
    return render(request,"himalaya/una.html",context={})
def kullu(request):
    return render(request,"himalaya/kullu.html",context={})
def mandi(request):
    return render(request,"himalaya/mandi.html",context={})
def shimla(request):
    return render(request,"himalaya/shimla.html",context={})
def lahual_spiti(request):
    return render(request,'himalaya/lahua&spiti.html',context={})