from django.urls import path 
from app2.views import *

app_name="connet2"

urlpatterns = [
    path('country/',country,name='country'),
    # path('insert_into_country/',insert_into_country,name='insert_into_country'),

    path('capital/',capital,name='capital'),
    # path('insert_into_capital/',insert_into_capital,name='insert_into_capital'),
]