from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Project , task
from django.shortcuts import get_object_or_404 #para evitar que se caiga y vote error
from django.shortcuts import render #para improtar htmls
 
def index(resquest):
    username = 'Byvagner'
    return render( resquest , 'index.html' , {
        'myname': username
    })


def projects(request):
    dateProjects = Project.objects.all()
    return render(request , 'projects.html' , {
        'projects': dateProjects
    })


def tasks(request ):
    dateTasks = task.objects.all()
    return render(request , 'tasks.html' , {
        'tasks': dateTasks
    })

