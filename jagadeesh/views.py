from django.shortcuts import render

# Create your views here.

def asif(request):
    return render(request,'asif.html',context={'name':'asif'})