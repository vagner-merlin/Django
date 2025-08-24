from django.urls import path 
from . import views
#aca cramos un archivo urls para poner todas las rutas aca de nuestra aplicacion 
urlpatterns = [
    path('', views.index),
    path('projects/', views.projects),
    path('tasks/', views.tasks),
]
