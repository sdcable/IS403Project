from django.http import HttpResponse
from django.shortcuts import render

def Home(request) :
    return render(request, 'homepages/index.html') #This will be our opening home page

def Spencer(request):
    return render(request, 'Activities/SpencerPage.html') #This will be Spencer's page

def Darby(request):
    return render(request, 'Activities/DarbyPage.html') #This will be Darby's Page

def Megan(request):
    return render(request, 'Activities/MeganPage.html') #This will be megans change

def Carter(request):
    return render(request, 'Activities/CarterPage.html') #This will be Carter's page :))))))