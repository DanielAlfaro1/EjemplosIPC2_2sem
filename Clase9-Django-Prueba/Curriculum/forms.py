from django import forms

class ArchivoConfiguracion(forms.Form):
    nombre = forms.CharField(max_length=50)
    archivo = forms.FileField()