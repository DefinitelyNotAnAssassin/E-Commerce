from django.shortcuts import render, HttpResponse

# Create your views here.


def index(request):
    if request.method == "GET":
        if request.user.is_authenticated:
            return render(request, 'UserInterface/index.html')
        else:      
            return render(request, 'UserInterface/index_user.html')
    else: 
        HttpResponse("Invalid Request")
        
