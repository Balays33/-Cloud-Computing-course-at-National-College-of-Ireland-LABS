from django.db import models

# Create your models here.

class Feed(models.Model):
    # each class variable represents a database i.e. table field in the model
    titleF = models.CharField(max_length=60)
    descriptionF = models.CharField(max_length=200,default="No description")
    locationF = models.CharField(max_length=60,default="Dublin")
    createdTimeF = models.DateTimeField(auto_now_add=True, blank=True)
    #uploadTimeF = models.CharField(max_length=60,default="time")
    uploadTimeF = models.DateTimeField(auto_now_add=True, blank=True)
    weatherF = models.CharField(max_length=20,default="no info yet")
    weatherdescriptionF = models.CharField(max_length=20,default="-")
    weatericonF = models.CharField(max_length=20,default="-")
    #uploadTimeF = models.DateTimeField(auto_now=True)
    #pictureF = models.FileField(upload_to='media/',default='settings.MEDIA_ROOT/apple.jpg')
    pictureF = models.ImageField(null=True, blank =True, upload_to = "images/")
    
    def __str__(self):
        return self.titleF + " - " + self.descriptionF + " - " + self.locationF 
    
    
        

class Todo(models.Model):
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return self.title


   