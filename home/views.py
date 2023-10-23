from django.shortcuts import render, get_object_or_404
from .models import Products
from purchase.models import CartItem, Cart


# Main page
def home(request):
	data = {'products': Products.objects.all()}
	return render(request, 'home/home.html', data)

# Product listing
def listing(request, slug_url):
	obj = get_object_or_404(Products, slug=slug_url)
	return render(request, 'home/listing.html', {'obj': obj})



