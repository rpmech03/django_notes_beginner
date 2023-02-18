from ctypes import addressof
import email
import random
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import redirect, render
import requests
def home(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        sal=request.POST['sal']
        d={
            'name':name,
            'email':email,
            'address':address,
            'sal':sal
        }
        r=requests.post("https://djrestpp.herokuapp.com/emps/",d)
    data=requests.get("https://djrestpp.herokuapp.com/emps/")
    print(data.json())
    return render(request,"index.html",{'data':data.json()})
def delete(request):
    id=request.GET['id']
    requests.delete("https://djrestpp.herokuapp.com/emps/"+id)
    data=requests.get("https://djrestpp.herokuapp.com/emps/")
    return render(request,"index.html",{'data':data.json()})
def search(request):
    id=request.POST['id']
    data=requests.get("https://djrestpp.herokuapp.com/emps/"+id)
    #data=requests.get("https://djrestpp.herokuapp.com/emps/")
    return render(request,"result.html",{'data':data.json()})
def update(request):
    id=request.POST['id']
    name=request.POST['name']
    email=request.POST['email']
    address=request.POST['address']
    sal=request.POST['sal']
    d={
            'name':name,
            'email':email,
            'address':address,
            'sal':sal
    }
    requests.put("https://djrestpp.herokuapp.com/emps/"+id+"/",d)
    data=requests.get("https://djrestpp.herokuapp.com/emps/")
    return render(request,"index.html",{'data':data.json()})
def sendmail(request):
    if request.method=='POST':
        subject = 'otp'
        t=random.random()
        t=t*10000
        t=int(t)
        message = str(t)
        email_from = settings.EMAIL_HOST_USER
        email=request.POST['email']
        recipient_list = [email, ]
        send_mail( subject, message, email_from, recipient_list )
        return render(request,'confirm.html',{'otp':t})
    else:
        return render(request,'sendmail.html')
def verify(request):
    otp=request.POST['otp']
    votp=request.POST['votp']
    if otp==votp:
        return render(request,'enterdetails.html')
    else:
        return render(request,'sendmail.html')