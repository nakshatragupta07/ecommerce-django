from django.shortcuts import render, HttpResponse, redirect
from .models import Product
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
# Create your views here.

def ecommerce(request):
    return render(request,'e-commerce.html')

def loginhandle(request):
     if request.method == "POST":
        name = request.POST['username']
        password = request.POST['password']
        user=authenticate(username=name,password=password)
        print(user,'user>>><<<')
        if user is not None:
         login(request,user)
         return redirect('/')
     

     return render(request,'login.html')

def signuphandle(request):
    if request.method == "POST":
        name = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username = name).first():
             messages.success(request,'account is already present')
        else:
            user = User(username=name,email=email)
            user.set_password(password)
            user.save()
            messages.success(request,'account created sucessfully')
            print(name,email,password)

        # user = User(username=name,email=email)
        # user.set_password(password)
        # user.save()
        # messages.success(request,'account created sucessfully')
        # return HttpResponse('your account is sucessfully created')

    return render(request,'signup.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')

def productdescription(request,id):
    get_data = Product.objects.filter(id=id)
    context = {

        'data':get_data
    }
    print(get_data)
    return render(request,'productdescription.html',context)

# def men(request):
#     data = Product.objects.all()
#     for i in data:
#         print(i.title)
#     return render(request,'men.html')


def men(request):
    # data = Product.objects.all()
    data = Product.objects.filter(cateogry="Men")
    context = {
        'data':data
    }
    return render(request,'men.html',context)


def women(request):
    # data = Product.objects.all()
    data = Product.objects.filter(cateogry="Women")
    context = {
        'data':data
    }
    return render(request,'women.html',context)
