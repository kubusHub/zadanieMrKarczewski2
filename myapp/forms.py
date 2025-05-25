from django import forms

class DataForm(forms.Form):
    N = forms.FloatField(label="ratio of Nitrogen in soil", min_value=0)
    P = forms.FloatField(label="ratio of Phosphorous in soil", )
    K = forms.FloatField(label="ratio of Potassium in soil", min_value=0)
    temperature = forms.FloatField(label="temperature (°C)")
    humidity = forms.FloatField(label="humidity in %", min_value=0, max_value=99.9)
    ph = forms.FloatField(label="ph of the soil", min_value=0, max_value=14)
    rainfall = forms.FloatField(label="rainfall (mm)", min_value=0)

