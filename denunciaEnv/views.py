from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'index.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def eventos(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'index.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def proyectos(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'index.html', 
                  { 'mapbox_access_token': mapbox_access_token })
