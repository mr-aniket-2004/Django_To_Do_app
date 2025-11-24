from django.shortcuts import render, redirect , get_object_or_404
from .models import Task

# Create your views here.

def home(request):
    task =Task.objects.all().order_by("created_at")
    return render(request, "subpages/home.html",{"task":task})

def add_task(request):

    if request.method =="POST":
        title = request.POST.get("title")
        description = request.POST.get("Description")
        if title :
            Task.objects.create(title =title,description= description)
            return redirect("home")
        else:
            error = "Title cannot be Empty"
            return render(request, "subpages/add_task.html",{"error":error})
            
    return render(request, "subpages/add_task.html")

def edit_task(request):
    return render(request, "subpages/edit_task.html")

def delete_task(request, list_id):
    task = get_object_or_404(Task, id=list_id)
    return render(request, "subpages/delete_task.html",{"task":task})
