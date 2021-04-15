from django.shortcuts import render, redirect
from django.http import HttpResponse
from todo.models import Tasks
from todo.forms import TasksForm  

# Create your views here.
def home(request):
    context = {'success': False}
    if request.method == "POST":
        title = request.POST['title']
        desc = request.POST['desc']
        ins = Tasks(taskTitle=title, taskDesc=desc)
        ins.save()
        context = {'success': True}
    return render(request, 'index.html', context)

def tasks(request):
    allTasks = Tasks.objects.all()
    #print(allTasks)
    #for item in allTasks:
        #print(item.taskTitle)

    context = {'tasks': allTasks}
    return render(request, 'tasks.html', context)

def destroy(request, id):
    task = Tasks.objects.get(id=id)
    task.delete()
    return redirect("/tasks")




