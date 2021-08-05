from django.shortcuts import render

def home_page(request):
    return render(request,'home.html')

def index(request):
    return render(request, 'index.html')


def my_bio(request):
    return render(request, 'my_bio.html')
 