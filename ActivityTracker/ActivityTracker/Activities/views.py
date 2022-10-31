from django.http import HttpResponse

def Home(request) :
    return HttpResponse('Hello Universe!') #This will be our opening home page

def Spencer(request):
    return HttpResponse('Hello Spencer!') #This will be Spencer's page

def Darby(request):
    return HttpResponse('Hello Darby! Welcome to your page!') #This will be Darby's Page

def Megan(request):
    return HttpResponse('Hello Megan!')

def Carter(request):
    return HttpResponse('Hello Carter! test')