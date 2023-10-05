from django.shortcuts import render

# Create your views here.
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/pagina.html', {})

def SegundaPagina(request):
    return render(request, 'PaginaconCSS/pagina.html', {})