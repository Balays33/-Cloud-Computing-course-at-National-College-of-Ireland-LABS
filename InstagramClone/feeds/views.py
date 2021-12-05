from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404

from . import s3storage as s3module

#time package import
import time



#Todo model import
from .models import Todo
from .models import Feed

# Create your views here.




'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''


def index(request):
    print("index page")
    timeGet()
    print(timeGet())
    context= {}
    context['val'] = timeGet()
    print(context)   
    
    
    feeds_database = Feed.objects.all()
    if request.method == 'POST':
        new_feed = Feed(
            titleF = request.POST['titleF'],
            descriptionF = request.POST['descriptionF'],
            uploadTimeF = request.POST['uploadTimeF'],
            #pictureLink = request.POST['pictureLink'],
            )
        new_feed.save()
    
        
    
    return render(request, 'feeds/index.html', {'feeds_database': feeds_database, 'context': context})
    


def developer(request):
    print("developer python fuction")
    
    
    
    context= {}
    context['val'] = "TEST"
    #context['s3test'] = s3module.printOutTest('intagramclone2021')
    #context['s3test'] = s3module.ListalltheobjectsinBucket('us-east-1','intagramclone2021')
    print(context)
    
    todo = Todo.objects.all()
    if request.method == 'POST':
        new_todo = Todo(
            title = request.POST['title']
        )
        new_todo.save()
        #return redirect('/')        
        #return render(request, 'feeds/developer.html',{'todos' : todo}) 
        
            
    return render(request, 'feeds/developer.html', {'todos' : todo ,'context': context})
        
        

    
def delete(request, pk):
    print("delete python fuction")
    todo = Todo.objects.get(id=pk)
    todo.delete()
    
    return render(request, 'feeds/developer.html', )
    
# upload time get from the Python package    
def timeGet():
    seconds = time.time()
    local_time = time.ctime(seconds)
    print("Local time:", local_time)
    
    return local_time 
    
    
