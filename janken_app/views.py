from django.shortcuts import render

# Create your views here.

def result(request):
    return render(request, "janken/result.html")

def janken(request):
    return render(request, "janken/janken.html")
