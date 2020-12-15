from django import forms
from django.forms import ModelForm
from .models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('title', 'content', 'created', 'priority', 'due_date', 'category', 'completed',) # include all fields in form
        # fields=('title','completed') # include particular fileds of model in form

        #We can add widgets to forms to treat them like html elements
        widgets = {
            'title': forms.TextInput(attrs = {'class': 'form-control'}),
            'content': forms.Textarea(attrs = {'class': 'form-control'}),
            'created': forms.DateTimeInput(attrs={'readonly':'readonly'}),
            'due_date': forms.DateTimeInput(attrs = {'class': 'form-control', 'type': 'datetime'}),
            'completed': forms.CheckboxInput(),
            'category': forms.Select(attrs = {'class': 'form-control'}),
        }