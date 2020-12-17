from django.shortcuts import render, HttpResponse, redirect
from .forms import TaskForm
from .models import Task, Category


#index url in the main page of the app
def index(request):

    tasks = Task.objects.all().order_by("completed", "-created")

    categories = Category.objects.all() #getting all categories with object manager

    #if request had post
    if request.method == "POST":

        #if taskAdd in the request
        if "taskAdd" in request.POST:
            new_title = request.POST["title"]
            new_due_date = request.POST["due_date"]
            new_content = request.POST["content"]
            new_priority = request.POST["priority"]
            new_category = request.POST["category"] #category

            #creating new Task object
            new_Task = Task(title = new_title, content = new_content, priority = new_priority, due_date= new_due_date, category=Category.objects.get(name=new_category))

            #saving the database
            new_Task.save()
        return redirect("index") #reloading the page

    #Send render to index.html with task objects, category objects and a range from 1,5 for priority selection
    return render(request, "index.html", {"tasks": tasks, "categories":categories, 'n' : range(1, 6, 1)})


#for updating tasks, get request and primary key of the task
def update_task(request, pk):

    #find the the object using primary key
    task = Task.objects.get(id=pk)

    #create a form
    form = TaskForm(instance=task)

    if request.method == "POST":
        #create form
        form = TaskForm(request.POST, instance=task)

        #get all the fields from the request and as a form save all of the to database
        if form.is_valid():
            form.save()
            return redirect("index")

    return render(request, "update_task.html", {"task_edit_form": form})

#delete view gets the primary key of the task and gets the task from Task objects, then deletes it from database
def delete_task(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return redirect("index")


#complete task recives the id of the task and marks that task object as completed
def complete_task(request, pk):
    task = Task.objects.get(id=pk)

    if task.completed == True:
         task.completed = False
    else:
        task.completed = True

    task.save()
    return redirect("index")



#recies multiple request for sorting and according to what request was recived it will
#return sorted task list and it will render it
def sort_task(request):

    #by defualt sort tasks by created date ascending
    tasks = Task.objects.all().order_by("-created")

    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST":
        if "due_date" in request.POST:
            tasks = Task.objects.all().order_by("completed", "due_date")
            redirect("index")

        if "priority" in request.POST:
            tasks = Task.objects.all().order_by("completed", "-priority")
            redirect("index")

        #delete all completed tasks
        if "delete_completed" in request.POST:
            for task in tasks:
                if task.completed == True:
                    delete_task = Task.objects.get(id = task.id)
                    delete_task.delete()
            tasks = Task.objects.all().order_by("completed","-created")
            redirect("index")

    return render(request, "index.html", {"tasks": tasks, "categories":categories, 'n' : range(1, 6, 1)})

