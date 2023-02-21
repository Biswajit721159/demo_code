from django.shortcuts import render, HttpResponse, redirect
from .models import Product, Photo, order
from django.contrib.auth. models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
# Create your views here.

data = Product.objects.all()
product = {
    'product': data
}


def index(request):

    return render(request, "shop/dashboard.html", product)


def about(request):
    return HttpResponse("we are in about")


def contact(request):
    return HttpResponse("we are in contact")


def tracker(request):
    return HttpResponse("we are in tracker")


def search(request):
    return HttpResponse("we are in search")


def productview(request):
    return HttpResponse("we are in productview")


def checkout(request):
    return HttpResponse("we are in checkout")


def base(request):
    return render(request, "shop/base.html")


def submit(request):
    photo = request.POST.get('photo')
    data = Photo(
        photo=photo
    )
    data.save()
    return redirect('submit/show', "show.html")


def show(request):
    data = Photo.objects.all()
    product = {
        'product': data
    }
    return render(request, "shop/show.html", product)


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


def handellogout(request):
    logout(request)
    return redirect('/')


def orderdetail(request, id, username):
    data = order.objects.all()
    if len(username) != 0:
        count = 0
        for i in data:
            if i.username == username and i.orderid == id:
                count+=1
        print(count)        
        if count==0:
            add = order(
                username=username,
                orderid=id
            )
            add.save()
            count=0
            return redirect('/')     
        else:
            return HttpResponse("this product is already in your bag")   
    else:
        return HttpResponse("Please log in first---")


def orderhistory(request, username):
    if len(username) != 0:
        data = order.objects.all()
        product = []
        for i in data:
            if i.username == username:
                product.append(i)
        context = {'product': product}
        return render(request, "shop/show.html", context)
    else:
        return HttpResponse("wait bro")

def demo(request):
    return HttpResponse("just for demo")