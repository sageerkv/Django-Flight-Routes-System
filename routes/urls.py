from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_node, name="add_node"),
    path("nth/", views.find_nth_node, name="find_nth_node"),
    path("", views.reports, name="reports"),
]
