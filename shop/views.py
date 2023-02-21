from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Photo, order
from django.contrib.auth. models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def index(request):
    return render(request, "shop/Admin_login.html")

def connect(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/dashboard')
        else:
            return HttpResponse("unsuceessfull login")
    return HttpResponse("Something is wrong")

def dashboard(request):
    user=User.objects.all()
    context={
        'Total_admin':len(user)
    }
    return render(request,"shop/dashboard.html",context)

def handellogout(request):
    logout(request)
    return redirect('/dashboard')



def handelsignup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        user = User.objects.all()
        count = 0
        for i in user:
            if i.username == username:
                count += 1
        if count == 0:
            if len(username) != 0 and len(firstname) != 0 and len(lastname) != 0:
                if pass1 == pass2 and len(pass1) != 0:
                    myuser = User.objects.create_user(username, email, pass1)
                    myuser.first_name = firstname
                    myuser.last_name = lastname
                    myuser.save()
                    return HttpResponse("Your account has been successfully created--")
                else:
                    return HttpResponse("password && confarm password is not same--")
            else:
                return HttpResponse("please filled the the blanks before submit--")
        else:
            return HttpResponse("username is already exit--")

    else:
        return HttpResponse("404 page not found")

def handellogin(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return HttpResponse("unsuceessfull login")
    else:
        return HttpResponse("404 page not found")


