import os
import pickle
import numpy as np
from django.shortcuts import render
from django.conf import settings
from .forms import DataForm


def predict_plant(request):
    if request.method == 'POST':
        form = DataForm(request.POST)
        if form.is_valid():
            try:
                # Load model
                with open('myapp/datasets/knn_model.pkl', 'rb') as f:
                    model = pickle.load(f)

                # Prepare features
                features = np.array([[
                    float(form.cleaned_data['N']),
                    float(form.cleaned_data['P']),
                    float(form.cleaned_data['K']),
                    float(form.cleaned_data['temperature']),
                    float(form.cleaned_data['humidity']),
                    float(form.cleaned_data['ph']),
                    float(form.cleaned_data['rainfall']),
                ]])

                prediction = model.predict(features)
                crop_mapping = {
                    1: "Rice",
                    2: "Maize",
                    3: "Chickpeas",
                    4: "Kidneybeans",
                    5: "Pigeonpeas",
                    6: "Mothbeans",
                    7: "Mungbean",
                    8: "Blackgram",
                    9: "Lentil",
                    10: "Pomegranate",
                    11: "Banana",
                    12: "Mango",
                    13: "Grapes",
                    14: "Watermelon",
                    15: "Muskmelon",
                    16: "Apple",
                    17: "Orange",
                    18: "Papaya",
                    19: "Coconut",
                    20: "Cotton",
                    21: "Jute",
                    22: "Coffee"
                }
                predicted_crop = crop_mapping.get(prediction[0], "Unknown")


                return render(request, 'heart.html', {
                    'prediction': f"Recommended crop: {prediction[0]}",
                    'form': form
                })

            except Exception as e:
                return render(request, 'heart.html', {
                    'form': form,
                    'error': f"Prediction failed: {str(e)}"
                })
    else:
        form = DataForm()
    return render(request, 'heart.html', {'form': form})