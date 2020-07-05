from django.shortcuts import render

from app.models import *

from app.form import *
# Create your views here.
def c(request):
    c1 = category.objects.all()
    return render(request,'h1.html',context={'c1':c1})

def f(request):
    f1 = flipkart.objects.all()
    return render(request,'h2.html',context={'f1':f1})

def az(request):
    a1 = amazon.objects.all()
    return render(request,'h3.html',context={'a1':a1})

def cus(request):
    cus1 = customer.objects.all()
    return render(request,'h4.html',context={'cus1':cus1})

def fc(request):
    form = mcat()
    if request.method == 'POST':
        form = mcat(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'f_c.html',context={'form':form})

def ff(request):
    form = mflip()
    if request.method == 'POST':
        form = mflip(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'f_c.html',context={'form':form})

def fa(request):
    form = mzon()
    if request.method == 'POST':
        form = mzon(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'f_c.html',context={'form':form})

def fcus(request):
    form = mcustom()
    if request.method == 'POST':
        form = mcustom(request.POST)
        if form.is_valid():
            form.save()
    return render(request,'f_c.html',context={'form':form})

def log(request):
    return render(request,'flipkart.html')

