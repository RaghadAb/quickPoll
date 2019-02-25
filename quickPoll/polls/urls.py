
from django.urls import path
from . import views

urlpatterns = [
     path('search/', views.search), #when the user searches for specific polls

       ]

