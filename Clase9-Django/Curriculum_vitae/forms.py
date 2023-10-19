from django import forms

class Formulario_Diccionario(forms.Form):
    archivo = forms.FileField()