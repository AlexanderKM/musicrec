from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from bands.models import Band

def index(request):
    return render(request, "index.html", {
        "nav_page": "index",
    })

def bandName(request, band_id):
    
    try:
        band = get_object_or_404(Band, pk=band_id)
    except:
        raise Http404
    
    bands = Band.objects.filter(related=band)
    
    return render(request, "view_band.html", {
        "main_band": band,
        "bands":bands,
        "nav_page": "search",
    })
    
def search(request):
    return render(request, "search.html", {
        "nav_page": "search",
    })
    
def contact(request):
    return render(request, "contact.html", {
        "nav_page": "contact",
    })
