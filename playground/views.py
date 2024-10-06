from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse('Hello Everyone')
    age = 10+15
    return render(request,"hello.html",{"age":age})