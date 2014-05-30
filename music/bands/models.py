from django.db import models
    
class Genre(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField('date added')
    
    def __str__(self):
        return self.name
    
class Band(models.Model):
    name = models.CharField(max_length=50)
    date_added = models.DateTimeField('date added')
    genre = models.ForeignKey(Genre)
    
    def __str__(self):
        return self.name