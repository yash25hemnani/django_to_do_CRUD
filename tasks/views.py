from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *

# Create your views here.
def index(request):
    tasks = Task.objects.all()
    form = TaskForm

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    
    i = 1
    context = {'tasks': tasks, 'form':form, 'i':i}

    return render(request, 'tasks/list.html', context)

def updateTask(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        # If only request.POST is used, a new item will get created
        if form.is_valid():
            form.save()
        return redirect('/')
    
    context = {'form': form}
    return render(request, 'tasks/update_task.html', context)

def deleteTask(request, pk):
    item = Task.objects.get(id=pk)
    context = {'item':item}

    if request.method == 'POST':
        item.delete()
        return redirect('/')

    return render(request, 'tasks/delete.html', context)

def completeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = True
    task.save()
    return redirect('/')

def resumeTask(request, pk):
    task = Task.objects.get(id=pk)
    task.complete = False
    task.save()
    return redirect('/')
