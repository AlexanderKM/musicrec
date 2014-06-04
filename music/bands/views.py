from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render
from bands.models import Band
from bands.forms import SearchBandForm

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
    if request.method == 'POST':
        form = SearchBandForm(request.POST)
        if form.is_valid():
            bandName = form.cleaned_data['bandName']
            
            band = Band.objects.filter(name=bandName)
            
            bands = Band.objects.filter(related=band)
            
            print("hey")
            
            return render(request, "view_band.html", {
                "main_band": band,
                "bands":bands,
                "nav_page": "search",
            })
            
    else:
        form = SearchBandForm()
        
    return render(request, "search.html", {
        "nav_page": "search",
        "form": form,
    })
    
def contact(request):
    return render(request, "contact.html", {
        "nav_page": "contact",
    })
