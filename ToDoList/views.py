from django.shortcuts import render, HttpResponse
from .forms import TaskForm
from django.shortcuts import redirect
# Create your views here.


def index(request):
    # return HttpResponse("Hello World!!")
    form = TaskForm()
    if request.method == "POST":
        #Get the posted form
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("index.html")
    return render(request, "index.html", {"task_form": form})

