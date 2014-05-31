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
    
    return render(request, "view_band.html", {
        "band": band,
        "nav_page": "band",
    })
    
def search(request):
    return render(request, "search.html", {
        "nav_page": "search",
    })
