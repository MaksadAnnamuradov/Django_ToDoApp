from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task, Category



def index(request):
    # return HttpResponse("Hello World!!")
    tasks = Task.objects.all().order_by("due_date", "priority")

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
            return redirect("/") #reloading the page

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
    return redirect("/")


