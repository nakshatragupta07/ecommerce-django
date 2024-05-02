from django.shortcuts import render

# Create your views here.

def ecommerce(request):
    return render(request,'e-commerce.html')

def loginhandle(request):
    return render(request,'login.html')

def signuphandle(request):
    return render(request,'signup.html')

def checkout(request):
    return render(request,'checkout.html')

def cart(request):
    return render(request,'cart.html')