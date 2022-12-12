from django.urls import path
from .views import Home
from .views import ViewActivities
from .views import addActivities 
from .views import updateActivity
from .views import editActivity
from .views import deleteActivity


urlpatterns = [
    path("viewActivities/", ViewActivities, name="viewActivities"),
    path("addActivities/", addActivities, name="addActivity"),
    path("updateActivity/<int:activity_id>", updateActivity, name="updateActivity"),
    path("editActivity/<int:activity_id>", editActivity, name="editActivity"),
    path("deleteActivity/<int:activity_id>", deleteActivity, name='deleteActivity'),
    path("", Home, name="index"),   
]   