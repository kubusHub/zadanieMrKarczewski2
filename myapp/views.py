import os
import pickle
from django.shortcuts import render
from django.http import HttpResponse

def show_graph(request):
    with open('myapp/datasets/knn-heart.pkl', 'rb') as f:
        img_base64 = pickle.load(f)
    return render(request, 'heart.html', {'graph_base64': img_base64})


