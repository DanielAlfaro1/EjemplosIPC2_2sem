from django.shortcuts import render

# Create your views here.
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/pagina.html', {})

def PaginaconCSS(request):
    return render(request, 'PaginaEjemplo/pagina_con_css.html', {})