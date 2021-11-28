from django.db import models

# Create your models here.

class Feed(models.Model):
    # each class variable represents a database i.e. table field in the model
    titleF = models.CharField(max_length=60)
    descriptionF = models.CharField(max_length=200,default="No description")
    #uploadTimeF = models.CharField(max_length=60,default="time")
    uploadTimeF = models.DateTimeField(auto_now_add=True, blank=True)
    #uploadTimeF = models.DateTimeField(auto_now=True)
    #pictureLink = models.CharField(max_length=200)
    #pictureLink = models.URLField(max_length = 200)
    
    def __str__(self):
        return self.titleF + " - " + self.descriptionF  
    
    
        
        

class Todo(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title