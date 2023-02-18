from ctypes import addressof
import email
from django.shortcuts import render
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