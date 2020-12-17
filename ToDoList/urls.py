from django.urls import path
from . import views


#urls used in the project
urlpatterns = [
    path('',views.index,name="index"),
    path("sort_task", views.sort_task, name="sort_task"),
    path("update/<int:pk>/", views.update_task, name="update_task"),
    path("delete/<int:pk>/", views.delete_task, name="delete_task"),
    path("complete_task/<int:pk>/", views.complete_task, name="complete_task"),
]