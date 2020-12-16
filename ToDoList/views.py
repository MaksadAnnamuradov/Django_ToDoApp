from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task, Category



def index(request):
    # return HttpResponse("Hello World!!")
    tasks = Task.objects.all().order_by("completed", "-created")

    categories = Category.objects.all() #getting all categories with object manager

    if request.method == "POST":
        #Get the posted form
        if "taskAdd" in request.POST:
            new_title = request.POST["title"]
            new_due_date = request.POST["due_date"]
            new_content = request.POST["content"]
            new_priority = request.POST["priority"]
            new_category = request.POST["category"] #category

            new_Task = Task(title = new_title, content = new_content, priority = new_priority, due_date= new_due_date, category=Category.objects.get(name=new_category))
            #new_Task = Task(**dict(request.POST, category= Category.objects.get(name=new_category)))

            new_Task.save()
        return redirect("index") #reloading the page

    return render(request, "index.html", {"tasks": tasks, "categories":categories, 'n' : range(1, 6, 1)})



def update_task(request, pk):
    task = Task.objects.get(id=pk)

    form = TaskForm(instance=task)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "update_task.html", {"task_edit_form": form})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")

def complete_task(request, pk):
    task = Task.objects.get(id=pk)

    if task.completed == True:
         task.completed = False
    else:
        task.completed = True

    task.save()
    return redirect("index")


def sort_task(request):

    tasks = Task.objects.all().order_by("-created")

    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST":
        if "due_date" in request.POST:
            tasks = Task.objects.all().order_by("completed", "due_date")
            redirect("index")

        if "priority" in request.POST:
            tasks = Task.objects.all().order_by("completed", "-priority")
            redirect("index")

        if "delete_completed" in request.POST:
            for task in tasks:
                if task.completed == True:
                    delete_task = Task.objects.get(id = task.id)
                    delete_task.delete()
            tasks = Task.objects.all().order_by("completed","-created")
            redirect("index")

    return render(request, "index.html", {"tasks": tasks, "categories":categories, 'n' : range(1, 6, 1)})

