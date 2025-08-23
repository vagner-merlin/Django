from django.db import models

# Create  modelo de tablas 

class Project(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class task(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    #como lo aprendido en base de datos podemos relacionar las tablas 
    #en eeste caso queremos realacionar project con task
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    def __str__(self):
        return self.title