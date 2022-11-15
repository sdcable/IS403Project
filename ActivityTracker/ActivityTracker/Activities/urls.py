from django.urls import path
from .views import Home
from .views import Spencer
from .views import Darby
from .views import Megan
from .views import Carter



urlpatterns = [
    path("Spencer", Spencer, name="SpencerPage"),
    path("Darby", Darby, name="DarbyPage"),
    path("Megan", Megan, name="MeganPage"),
    path("Carter", Carter, name="CarterPage"),
    path("", Home, name="index"),   
]   