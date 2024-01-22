from django.shortcuts import render,HttpResponse
from .forms import UnhashForm
from .models import hashcatmode

def home(request): 
    return render(request, "home.html")


def unhash(request): 
    if request.method == 'POST': 
        form = UnhashForm(request.POST)
        if form.is_valid(): 
            print("hehe")
    else: 
        form = UnhashForm()
        
    return render(request,'unhash.html',{'form':form})