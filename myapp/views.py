from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return HttpResponse("<h1>Hello world</h1>")

def hola_perro(request):
    return HttpResponse("<h2>HOlaaaa</h2>")

