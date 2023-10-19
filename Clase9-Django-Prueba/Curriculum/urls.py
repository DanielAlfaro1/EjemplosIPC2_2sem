from django.urls import path
from . import views

urlpatterns = [
    path('Ejemplo1/', views.PrimeraPagina, name="PrimeraPagina"),
    path('Ejemplo1-css/', views.PaginaconCSS, name="PaginaCSS"),
    path('form-ejemplo/', views.PaginaArchivoConfiguracion, name="PaginaArchivoConfiguracion"),
    path('Palabras/', views.PaginaPalabras, name="PaginaPalabras")
]