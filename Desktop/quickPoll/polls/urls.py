from django.conf.urls import url
from . import views


app_name="polls"

urlpatterns = [
     url(r'^search/$', views.search, name='search'), #when the user searches for specific polls

     url(r'^option/(?P<quiPoll_id>\d+)/', views.option_Number,name='option'),
     url(r'^option/(?P<quiPoll_id>\d+)/vote/', views.vote, name='vote'),
     #url(r'^register/$', views.register, name='register')

]



