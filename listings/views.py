from django.shortcuts import render, get_object_or_404
from .models import Listing 
from django.core.paginator import Paginator
from .choices import state_choices, price_choices, bedroom_choices

def index(request):
    listings=Listing.objects.order_by('-listing_date').filter(is_published=True)
    paginator=Paginator(listings, 6)
    page_no=request.GET.get('page')
    page_obj=paginator.get_page(page_no)

    context = {
        'listings':page_obj
    }
    return render(request,'listings/listings.html', context)
def listing(request, listing_id):
    listing=get_object_or_404(Listing, pk=listing_id)

    
    context = {
        'listing': listing
    }
    return render(request,'listings/listing.html', context)
def search(request):

    list_filter=Listing.objects.order_by('-listing_date')

    # filter by keyword
    if 'keywords' in request.GET :
        keywords=request.GET['keywords']
        if keywords :
            list_filter=list_filter.filter(description__icontains=keywords ) 
    
     # filter by city
    if 'city' in request.GET :
        city=request.GET['city']
        if city :
            list_filter=list_filter.filter(city__iexact=city ) 

     # filter by state
    if 'state' in request.GET :
        state=request.GET['state']
        if state :
            list_filter=list_filter.filter(state__iexact=state ) 
     # filter by bedrooms
    if 'bedrooms' in request.GET :
        bedrooms=request.GET['bedrooms']
        if bedrooms :
            list_filter=list_filter.filter(bedrooms__lte=bedrooms ) 
    
     # filter by price
    if 'price' in request.GET :
        price=request.GET['price']
        if price :
            list_filter=list_filter.filter(price__lte=price ) 
    
    


    context = {
        'state_choices': state_choices ,
        'price_choices': price_choices ,
        'bedroom_choices':bedroom_choices , 
        'listings':list_filter,
        'values': request.GET
    }
    return render(request,'listings/search.html', context )
