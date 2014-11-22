from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, render, redirect
from bands.models import Band, Search
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
            lowerBandName = str(bandName).strip().lower()
            
            bands = Band.objects.filter(name__iexact=lowerBandName)
            
            if len(bands) > 0:
                actualBand=bands[0]
                
                searchObject = Search(band=actualBand)
                searchObject.save()
            
                return redirect("bandName", band_id = actualBand.id)
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
