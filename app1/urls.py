from django.urls import path 
from app1.views import *

app_name="connet1"

urlpatterns = [
    path('topic/', topic, name="topic"),
    # path('insert_into_topic/',insert_into_topic,name='insert_into_topic'),
]