from django.contrib import admin
from .models import Project,task 
# Register your models here.

#este codigo nos ayuda a guardar nuestros modelos  
admin.site.register(Project)

#llamamos a task para que aprezca en el panel de adm
admin.site.register(task)