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
    
def statistics(request):
    searches = Search.objects.all().order_by("date_searched").reverse()
    return render(request, "statistics.html", {
        "searches" : searches,
        "nav_page": "statistics",
    })
    
"""
Calculates most popular searches
"""
def getTopSearches():
    allSearches = Search.objects.all()
    countMap = dict()
    for search in allSearches:
        if search.band in countMap:
            countMap[search.band] = countMap[search.band] + 1
        else:
            countMap[search.band] = 1
            
    itemSet = countMap.items()
    
    sortedList = sortListBigToSmall(itemSet)
    
    return sortedList
            
def sortListBigToSmall(itemSet):
    itemsList = []
    for item in itemSet:
        itemsList.append(item)
    if len(itemsList) > 1:
        
        for i in range( 0, len( itemsList ) -1 ):
            currentItem = itemsList[i]
            currentCount = itemsList[i][1]
            k = i
            while k < len(itemsList) and currentCount < itemsList[k + 1][1]:
                tmp = itemsList[k + 1]
                itemsList[k + 1] = currentItem
                itemsList[k] = tmp
                k += 1
            
    return itemsList
    
    
    
