from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Place,Peoples
from django.contrib.auth.models import User
from django.contrib import messages ,auth

# Create your views here.
def index(request):
    obj = Place.objects.all()
    people = Peoples.objects.all()
    return render(request,('index.html'),{"place":obj,"people":people} )


def loginn(request):
        if request.method=='POST':
            username= request.POST['username']
            password = request.POST['password1']
            
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                return redirect('index')
            else:
                messages.info(request,"Invalid Credentials")
                return redirect ('login')
                
        return render(request,'Loginn.html' )    
                


def register(request):
    if request.method=='POST':
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['first_name']
        email = request.POST['email']
        password = request.POST['password1']
        cpassword = request.POST['password2']
        if password == cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username already in exist")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already in exist")
                return redirect('register')
            else:
                user =User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save()
                print("User Created")
                return redirect('login')
        else:
            messages.info(request,"Password not matched")
            return redirect('register')
        
    return render(request,'register.html' )

def logout(request):
    auth.logout(request)
    return redirect('index')