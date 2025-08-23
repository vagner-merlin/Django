from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from .models import Project , task
from django.shortcuts import get_object_or_404 #para evitar que se caiga y vote error
from django.shortcuts import render #para improtar htmls
 
def index(resquest):
    return render( resquest , 'index.html')


def projects(request):
    project = list(Project.objects.values())
    return JsonResponse(project, safe=False)

#aca jugaremos con los parametros 
# del modelo task obtenemos el id que pasmos por parametro que establecimos en la url 
# tambien concatenamos
def Tasks(request ):
    #tareas = get_object_or_404(task, id=id) #que salga error si no encuentra 
    return HttpResponse('tasks')

