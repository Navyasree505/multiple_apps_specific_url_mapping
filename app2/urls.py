from app2.views import *
from django.urls import path
app_name="everything"
urlpatterns=[
    path('virat/',virat,name='virat'),
    path('divilliers/',divilliers,name='divilliers'),
]