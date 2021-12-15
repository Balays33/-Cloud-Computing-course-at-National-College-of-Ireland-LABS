from django import forms
from .models import *


class FeedForm(forms.ModelForm):
  
    class Meta:
        model = Feed
        fields = ['titleF', 'descriptionF', 'locationF', 'weatherF', 'weatherdescriptionF', 'weatericonF', 'pictureF']
        

