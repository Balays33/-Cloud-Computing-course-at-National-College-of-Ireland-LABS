from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.index, name='index'),
    path('', views.basichtmlrender),
    path('delete/<str:pk>', views.delete, name='delete')
]