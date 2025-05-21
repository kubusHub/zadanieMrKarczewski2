from django.urls import path
from .views import show_graph

urlpatterns = [
    path('graph/', show_graph, name='show_graph'),
]