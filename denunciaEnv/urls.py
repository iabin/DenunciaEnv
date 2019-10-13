from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos', views.proyectos, name='proyecto'),
    path('eventos', views.eventos, name='eventos'),
    path('denuncias', views.hacer_denuncia, name='denuncias')
]