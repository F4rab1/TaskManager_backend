from django.urls import path
from . import views

urlpatterns = [
    path('tasks/', views.task_list),
    # path('tasks/due/<str:due_date>', views.task_list_by_due_date)
]