from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def virat(request):
    return HttpResponse('<h1><marquee>Best Batsman in the world</marquee></h1>')

def divilliers(request):
    return HttpResponse('<h1>Monster</h1>')