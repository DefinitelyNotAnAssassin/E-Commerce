from django.shortcuts import render
from Models.models import Product 
# Create your views here.

def search_product(request): 
    args = request.GET.get('search')
    Products = Product.objects.filter(name__icontains=args)
    return render(request, 'Products/products.html', {'Product': Products})
    
    
    
    
    