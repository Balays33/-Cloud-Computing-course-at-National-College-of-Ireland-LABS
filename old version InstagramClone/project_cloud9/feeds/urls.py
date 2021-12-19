from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('feeds', views.index),
    # path('feeds/<slug:feeds_slug>', views.feeds_details),
     # /feeds/id e.g. /feeds/1
    path('<int:feed_id>/', views.show, name='show'),
]