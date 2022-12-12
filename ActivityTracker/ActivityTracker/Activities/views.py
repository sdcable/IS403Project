from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import activity
from .models import person

def Home(request) :
    return render(request, 'homepages/index.html') #This will be our opening home page

def ViewActivities(request):
    data = person.objects.all()
    data2 = activity.objects.all()

    context = {
        'person': data,
        'activity': data2,
    }
    return render(request, 'Activities/viewActivities.html', context) #This will dynamically display info based on logged in user

def addActivities(request):
    if request.method == 'POST':
        persons = person.objects.get(netid=request.POST['username'])
        new_activity = activity()

        new_activity.activity_title = request.POST['activity_title']
        new_activity.activity_category = request.POST['activity_category']
        new_activity.activity_description = request.POST['activity_description']
        new_activity.personid = persons

        new_activity.save()

        data = person.objects.all()
        data2 = activity.objects.all()

        context = {
        'person': data,
        'activity': data2,
        }
        
        return redirect ('viewActivities')
    
def editActivity(request, activity_id) : #redirects to edit page
    data = activity.objects.get(id=activity_id)

    context = {
        "activity" : data
    }
    return render(request, 'Activities/editActivity.html', context)

def updateActivity(request, activity_id): #saves updated info
    if request.method == 'POST':
        persons = person.objects.get(netid=request.POST['personid'])
        this_activity = activity.objects.get(id=activity_id)

        this_activity.activity_title = request.POST['activity_title']
        this_activity.activity_category = request.POST['activity_category']
        this_activity.activity_description = request.POST['activity_description']
        this_activity.personid = persons

        this_activity.save()

    return redirect('viewActivities')

   
    
def deleteActivity(request, activity_id): #deletes activity
    data = activity.objects.get(id=activity_id)
    
    data.delete()
    
    return redirect('viewActivities')
