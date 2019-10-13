from django.shortcuts import render, redirect
from django.http import HttpResponse
from denunciaEnv.forms import EventoForm
from django.utils import timezone


def index(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'index.html', 
                  { 'mapbox_access_token': mapbox_access_token })


def eventos(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'sargazo.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def proyectos(request):
    mapbox_access_token = 'pk.eyJ1IjoiaWFiaW4iLCJhIjoiY2sxbjYza3QwMDdnZjNjczBsZGZ5bmIwNiJ9.RbB2BZN-uSD_er3o8vCW4g'
    return render(request, 'index.html', 
                  { 'mapbox_access_token': mapbox_access_token })

def hacer_denuncia(request):
    if request.method == "POST":
        form = EventoForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.timestamp = timezone.now()
            model_instance.save()
            return redirect('/')
            
    else:
        form = EventoForm()
        return render(request, "hacerDenuncia.html", {'form': form})