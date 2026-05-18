from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def index(request):
    return render(request,"main/index.html")

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, 'main/product_detail.html', {'product': product})