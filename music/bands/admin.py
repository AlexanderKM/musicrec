from django.contrib import admin
from bands.models import Genre, Band, Search

admin.site.register(Genre)
admin.site.register(Band)
admin.site.register(Search)