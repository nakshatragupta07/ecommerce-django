from django.shortcuts import render
from .models import Product

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
