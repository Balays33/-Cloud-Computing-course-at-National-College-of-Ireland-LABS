from django.urls import path

from . import views

urlpatterns = [
    path('developer', views.developer, name='developer'),
    
    # dynamic url to the delete todo
    path('', views.index, name='index'),
    path('delete/<str:pk>', views.delete, name='delete')
]