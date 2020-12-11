from django.shortcuts import render, HttpResponse, redirect

from .models import Task



def index(request):
    # return HttpResponse("Hello World!!")
    tasks = Task.objects.all()

    #categories = Category.objects.all() #getting all categories with object manager

    if request.method == "POST":
        #Get the posted form

        new_title = request.POST["title"]
        new_due_date = request.POST["due_date"]
        new_content = request.POST["content"]
        #new_category = request.POST["category"]

        new_Task = Task(title = new_title, content = new_content, due_date= new_due_date)
        new_Task.save()
        return redirect("/")
    return render(request, "index.html", {"tasks": tasks})



def update_task(request, pk):
    task = Task.objects.get(id=pk)

    #form = TaskForm(instance=task)

    if request.method == "POST":
        #form = TaskForm(request.POST, instance=task)
        #if form.is_valid():
        task.title = request.POST["title"]
        task.due_date = request.POST["due_date"]
        task.content = request.POST["content"]

        completed = request.POST.get('completed')
        completed = True if completed else False
        task.completed = completed

        task.save()
        return redirect("index")

    return render(request, "update_task.html", {"task": task})


def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")

