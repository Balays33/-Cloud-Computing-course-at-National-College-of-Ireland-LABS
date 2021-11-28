from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def sayhello(request):
    return HttpResponse("Hello, world")
    
#basic html render    
def basichtmlrender(request):
    return render(request, 'hello.html')
    
#pass the html a list
def passhtmlrender(request):
    return render(request, 'passvalue.html' , {'name' : 'Balazs'})




def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")