from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from bands.models import Band

def index(request):
    return HttpResponse("Hello, world.")

def bandName(request, band_id):
    
    band = get_object_or_404(Band, pk=band_id)
    
    return render(request, "view_band.html", {
        "band": band,
    })
