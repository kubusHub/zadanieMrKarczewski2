from django.urls import path
from . import views

urlpatterns = [
    path('heart/', views.predict_plant),

]