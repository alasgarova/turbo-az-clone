from django.shortcuts import render
from .models import Listing

def index(request):
    listings = Listing.objects.all()
    return render(request, 'core/index.html', {'listings': listings})