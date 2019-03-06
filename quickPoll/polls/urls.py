
from django.urls import path
from . import views


app_name="quickPoll"

urlpatterns = [
     path('search/', views.search, name='search'), #when the user searches for specific polls
]

