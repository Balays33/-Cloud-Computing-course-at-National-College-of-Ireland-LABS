from django.shortcuts import render
from django.http import HttpResponse
#from .models import feeds
from django.http import Http404
from .models import Feed

# Create your views here.

'''
def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")
'''
'''
def index(request):
    feeds = [
            {
                'title' : 'first feeds', 
                'location': 'new york', 
                'slug': 'a-first-meetup'
                
            },
            {
                'title' : 'second feeds', 
                'location': 'los angeles', 
                'slug': 'a-second-meetup'
                
            }
        ]
        
    newest_feeds = Feed.objects.order_by('-release_date')[:15]
    context = {'newest_feeds': newest_feeds}
    
    return render(request, 'feeds/index.html', {
        'show_feeds': True,
        'feeds': feeds
        
    },context)

    

def feeds_details(request, feeds_slug):
    print(feeds_slug)
    selected_feeds = {
            'title': 'A first feeds', 
            'description': 'this is the first feeds'
             }
    return render(request, 'feeds/feeds_details.html',{
        'selected_title': selected_feeds['title'],
        'description': selected_feeds['description']
    })
    
'''

def index(request):
    newest_feeds = Feed.objects.order_by('-release_date')[:15]
    context = {'newest_feeds': newest_feeds}
    return render(request, 'feeds/index.html', context)


def show(request, feed_id):
    try:
        feed = Feed.objects.get(pk=feed_id)
    except Feed.DoesNotExist:
        raise Http404("Feed does not exist")
    return render(request, 'feeds/feeds_details.html', {'feed': feed})
