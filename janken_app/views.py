from django.shortcuts import render
from .models import Janken
from django.utils import timezone

def janken(request):
    users = Janken.objects.filter(create_date__lte=timezone.now()).order_by('create_date')
    return render(request, "janken_app/janken.html", {'users': users})
