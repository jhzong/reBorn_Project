from django.shortcuts import render
from django.http import HttpResponse

def rlist(request):
    return render(request,'restaurants/rlist.html')
