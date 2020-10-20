from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse 

def index(request): 
    
    temp = 0
    for i in range(10):
        if i%2 == 0:
            temp += i
    strline = "hello shinhash and temp : " + str(temp)
    return HttpResponse(strline)



def detail(request):
    return render(request, "viewTest.html")

