from django.db import models
from django.conf import settings
import datetime
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return self.name
    
class Band(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField(default=datetime.datetime.now())
    genre = models.ForeignKey(Genre, blank=True)
    related = models.ManyToManyField("self", blank=True)
    
    #main_photo = models.ImageField(upload_to = settings.MEDIA_ROOT)
    
    def __str__(self):
        return self.name
    
class Search(models.Model):
    band = models.ForeignKey(Band)
    date_searched = models.DateTimeField(default=datetime.datetime.now())
    
    def __str__(self):
        return str(self.band) + " : " + str(self.date_searched)
    
    