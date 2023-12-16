from django.shortcuts import render,HttpResponse
from home.models import Task

# Create your views here.
# def home(request):
    # return HttpResponse('works')

def home(request):
    context = {'success':False}
    if request.method == "POST":
        # success is {{success}}
        title = request.POST["title"]
        desc = request.POST["desc"]
        print(title,desc)
        # creating a new task instance
        newInstance = Task(taskTitle = title, taskDesc = desc)
        newInstance.save()
        context = {'success':True}
    return render(request,'index.html',context)

def tasks(request):
    allTasks = Task.objects.all()
    context ={'tasks':allTasks}
    return render(request, 'tasks.html',context)
