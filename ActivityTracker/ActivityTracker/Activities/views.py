from django.http import HttpResponse
from django.shortcuts import render
from .models import activity

def Home(request) :
    return render(request, 'homepages/index.html') #This will be our opening home page

def Spencer(request):
    activities = activity.objects.filter(personid='1')

    context = {
        'hobbies': activities
    }

    return render(request, 'Activities/SpencerPage.html', context) #This will be Spencer's page

def Darby(request):
    return render(request, 'Activities/DarbyPage.html') #This will be Darby's Page

def Megan(request):
    return render(request, 'Activities/MeganPage.html') #This will be megans change

def Carter(request):
    return render(request, 'Activities/CarterPage.html') #This will be Carter's page :))))))

def samplesView(request):
    return render(request, 'Activities/samples.html')