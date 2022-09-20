from django.urls import path
from djangoProject101.task.views import show_bare_minimum_view, show_all_tasks, index

urlpatterns = (
    # http://localhost:8000/task/
    path('', index),
    # http://localhost:8000/task/it-works/
    path('it-works/', show_bare_minimum_view),
    # http://localhost:8000/task/all/
    path('all/', show_all_tasks),
)

