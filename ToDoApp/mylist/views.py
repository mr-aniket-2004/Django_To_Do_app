from django.shortcuts import render
from .models import Task

# Create your views here.

def home(request):
    task =Task.objects.all().order_by("created_at")
    return render(request, "subpages/home.html",{"task":task})