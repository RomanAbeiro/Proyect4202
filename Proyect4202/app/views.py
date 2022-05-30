from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'app/index.html')

def contacts(request):
    return render(request, 'app/contacts.html')

def photos(request):
    return render(request, 'app/photos.html')