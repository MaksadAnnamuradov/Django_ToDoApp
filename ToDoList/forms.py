from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = "__all__"  # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form

        #We can add widgets to forms to treat them like html elements