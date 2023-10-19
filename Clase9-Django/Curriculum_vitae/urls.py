from django.urls import path
from . import views

urlpatterns = [
    path('Ejemplo1/', views.PrimeraPagina, name="La primera pagina"),
    path('Ejemplo1-css/', views.SegundaPagina, name="La segunda pagina"),
    path('Form-Diccionario/', views.PaginaForm_Diccionario, name='Form Diccionario'),
    path('Diccionario/', views.Pagina_GetDiccionario, name="Pagina de palabras"),
]