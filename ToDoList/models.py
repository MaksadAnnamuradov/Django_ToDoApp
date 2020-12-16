from django.db import models
from django.utils import timezone
from datetime import datetime



class Category(models.Model): # The Category table name that inherits models.Model
    name = models.CharField(max_length=100, primary_key=True) #Like a varchar

    class Meta:
        verbose_name = ("Category")
        verbose_name_plural = ("Categories")

    def __str__(self):
        return self.name #name to be shown when called



# Create your models here.
class Task(models.Model):
    title=models.CharField(max_length=350)
    completed=models.BooleanField(default=False)
    content = models.TextField(blank=True)
    created = models.DateTimeField(default=timezone.now())
    priority = (models.IntegerField(default= 1))
    #due_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
    due_date = models.DateTimeField(null=False, blank=False)
    category = models.ForeignKey(Category, default="general", on_delete= models.CASCADE) # a foreignkey


    def __str__(self):
        return self.title

