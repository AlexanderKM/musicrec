from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
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
            
            bands = Band.objects.filter(name=bandName)
            
            if len(bands) > 0:
                band=bands[0]
            
            
            
                return redirect("bandName", band_id = band.id)
            else:
                error = "The band '" + bandName + "' was not found."
                return render(request, "search.html", {
                            "nav_page": "search",
                            "form": form,
                            "error":error,
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
