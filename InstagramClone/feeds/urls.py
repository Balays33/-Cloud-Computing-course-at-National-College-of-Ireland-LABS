from django.urls import path

from . import views

urlpatterns = [
    path('developer', views.developer, name='developer'),
    path('upload', views.upload, name='upload'),
    
    # dynamic url to the delete todo
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
]