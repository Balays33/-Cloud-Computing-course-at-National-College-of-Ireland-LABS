from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
import requests

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
    #print(timeGet())
    context= {}
    context['val'] = timeGet()
    #print(context['val'])   
    
    url =  'https://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=92757f89a5760a1310e7b5657fff90d2'
    
    city = "Dublin"
    
    r =requests.get(url.format(city)).json()
    
    city_weather = {
        'city' : city,
        'tempature' : r['main']['temp'],
        'description' : r['weather'][0]['description'] ,
        'icon' : r['weather'][0]['icon'],
    }
    
    context['city_weather'] = city_weather
    #print(context['city_weather'])
    feeds_database = Feed.objects.all()
    
    
    
    if request.method == 'POST':
        new_feed = Feed(
            titleF = request.POST['titleF'],
            descriptionF = request.POST['descriptionF'],
            uploadTimeF = request.POST['uploadTimeF'],
            locationF = request.POST.get('locationF', False),
            #locationF = request.POST['FFlocationF'],
            #pictureLink = request.POST['pictureLink'],
            )
        new_feed.save()
    weaterforcast(feeds_database,url)
    
    return render(request, 'feeds/index.html', {'feeds_database': feeds_database, 'context': context})
    


def developer(request):
    print("developer python fuction")
    
    
    
    context= {}
    context['val'] = "TEST"
    #context['s3test'] = s3module.printOutTest('intagramclone2021')
    context['s3test'] = s3module.ListalltheobjectsinBucket('us-east-1','intagramclone2021')
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
    
#update weather forecast
def weaterforcast(feeds_database,url):
    for updateWeatherDATA in feeds_database:
        citylocation =updateWeatherDATA.locationF
        print(citylocation)
        newGeoWeater =requests.get(url.format(citylocation)).json()
        print(newGeoWeater)
        try:
          print(newGeoWeater['main']['temp'])
          updateWeatherDATA.weatherF = newGeoWeater['main']['temp']
          updateWeatherDATA.save(update_fields=['weatherF'])
          updateWeatherDATA.weatherdescriptionF =  newGeoWeater['weather'][0]['description']
          updateWeatherDATA.save(update_fields=['weatherdescriptionF'])
          updateWeatherDATA.weatericonF = newGeoWeater['weather'][0]['icon']
          updateWeatherDATA.save(update_fields=['weatericonF'])
        except Exception as e:
          #print(e)
          print("ERROR")
          errorObject = feeds_database.get(locationF=citylocation)
          errorObject.delete()
    return feeds_database 
    
    
#clean up
    """
    
    
    
    def weaterforcast(feeds_database,url):
    for updateWeatherDATA in feeds_database:
        citylocation =updateWeatherDATA.locationF
        print(citylocation)
        newGeoWeater =requests.get(url.format(citylocation)).json()
        iftestet = str(requests.get(url.format(citylocation)).json())
        print(newGeoWeater)
        if iftestet == '{"cod":"404","message":"city not found"}':
            print("ERROR newGeoWeater")
        else:
            print(newGeoWeater['main']['temp'])
            updateWeatherDATA.weatherF = newGeoWeater['main']['temp']
            updateWeatherDATA.save(update_fields=['weatherF'])
            updateWeatherDATA.weatherdescriptionF =  newGeoWeater['weather'][0]['description']
            updateWeatherDATA.save(update_fields=['weatherdescriptionF'])
            updateWeatherDATA.weatericonF = newGeoWeater['weather'][0]['icon']
            updateWeatherDATA.save(update_fields=['weatericonF'])
        
    return feeds_database
    for weaterCity in feeds_database:
        #weatherF = feeds_database.get(titleF='telex')
        feeds_database.weatherF.weaterCity = "Balazs"
        print(feeds_database.weatherF)
     
     t = feeds_database.get(titleF='telex')
    t.weatherF = 999  # change field
    t.save() # this will update only
     
    
   
  
    for each in Feed.objects.all():
        tr = feeds_database.all()
        tr.weatherF =333
        tr.save()
        #test = each.weatherF
        #each.weatherF.save()
        print(each.weatherF)
       
    for updateWeatherDATA in feeds_database:
        updateW = feeds_database.updateWeatherDATA
        updateW.weatherF = 22
        updateW.save()
        
    myQuery = Feed.objects.all()
    for item in myQuery:
        item.weatherF = 55
        item.save(update_fields=['weatherF'])
        
        
    entry_list = list(Feed.objects.all())
    entry_list[0].titleF = "David"
    print(entry_list[0].titleF)
    
    Feed.objects.all()[0].titleF = "David"
    
    print(Feed.objects.all()[0].titleF)

    
    
   
    for updateWeatherDATA in feeds_database:
        citylocation =updateWeatherDATA.locationF
        #print(citylocation)
        newGeoWeater =requests.get(url.format(citylocation)).json()
        #print(newGeoWeater['main']['temp'])
        updateWeatherDATA.weatherF = newGeoWeater['main']['temp']
        updateWeatherDATA.save(update_fields=['weatherF'])
        updateWeatherDATA.weatherdescriptionF =  newGeoWeater['weather'][0]['description']
        updateWeatherDATA.save(update_fields=['weatherdescriptionF'])
        updateWeatherDATA.weatericonF = newGeoWeater['weather'][0]['icon']
        updateWeatherDATA.save(update_fields=['weatericonF'])
    """