from django.shortcuts import render, HttpResponse

# Create your views here.

def add_product(request):
    if request.method == "GET":
        return render(request, 'API/add_product.html')
    else: 
        HttpResponse("Invalid Request")
        
def edit_product(request):
    if request.method == "GET":
        return render(request, 'API/edit_product.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_product(request):
    if request.method == "GET":
        return render(request, 'API/delete_product.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_review(request):
    if request.method == "GET":
        return render(request, 'API/add_review.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_review(request):
    if request.method == "GET":
        return render(request, 'API/delete_review.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_cart(request):
    if request.method == "GET":
        return render(request, 'API/add_cart.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_cart(request):
    if request.method == "GET":
        return render(request, 'API/delete_cart.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_wishlist(request):
    if request.method == "GET":
        return render(request, 'API/add_wishlist.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_wishlist(request):
    if request.method == "GET":
        return render(request, 'API/delete_wishlist.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_payment(request):
    if request.method == "GET":
        return render(request, 'API/add_payment.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_payment(request):
    if request.method == "GET":
        return render(request, 'API/delete_payment.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_order(request):
    if request.method == "GET":
        return render(request, 'API/add_order.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_order(request):
    if request.method == "GET":
        return render(request, 'API/delete_order.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_shipping_address(request):
    if request.method == "GET":
        return render(request, 'API/add_shipping_address.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_shipping_address(request):
    if request.method == "GET":
        return render(request, 'API/delete_shipping_address.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_contact(request):
    if request.method == "GET":
        return render(request, 'API/add_contact.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_contact(request):
    if request.method == "GET":
        return render(request, 'API/delete_contact.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_category(request):
    if request.method == "GET":
        return render(request, 'API/add_category.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_category(request):
    if request.method == "GET":
        return render(request, 'API/delete_category.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_coupon(request):
    if request.method == "GET":
        return render(request, 'API/add_coupon.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_coupon(request):
    if request.method == "GET":
        return render(request, 'API/delete_coupon.html')
    else: 
        HttpResponse("Invalid Request")
        
def edit_coupon(request):
    if request.method == "GET":
        return render(request, 'API/edit_coupon.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_refund(request):
    if request.method == "GET":
        return render(request, 'API/add_refund.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_refund(request):
    if request.method == "GET":
        return render(request, 'API/delete_refund.html')
    else: 
        HttpResponse("Invalid Request")
        
def add_order_item(request):
    if request.method == "GET":
        return render(request, 'API/add_order_item.html')
    else: 
        HttpResponse("Invalid Request")
        
def delete_order_item(request):
    if request.method == "GET":
        return render(request, 'API/delete_order_item.html')
    else: 
        HttpResponse("Invalid Request")
        
    