from django.shortcuts import render
from .forms import ArchivoConfiguracion
from django.http import HttpResponseRedirect
import requests

# Create your views here.
def PrimeraPagina(request):
    return render(request, 'PaginaEjemplo/pagina.html', {})

def PaginaconCSS(request):
    return render(request, 'PaginaEjemplo/pagina_con_css.html', {})

def PaginaArchivoConfiguracion(request):
    if request.method == "POST":
        print("es post")
        form = ArchivoConfiguracion(request.POST, request.FILES)
        if form.is_valid():
            print(request.FILES['archivo'].read().decode('utf-8'))
            arregloJson = {
                'contenido' : request.FILES['archivo'].read().decode('utf-8')
            }
            url = 'http://127.0.0.1:3000/post-archivo-conf'
            r = request.post(url, data=arregloJson)
            
            return HttpResponseRedirect("/cv/Palabras/")
    else:
        form = ArchivoConfiguracion()
    return render(request, "PaginaEjemplo/form_arch_conf.html", {"form":form})

def PaginaPalabras(request):
    url = 'http://127.0.0.1:3000/get-palabras'
    r = request.get(url)
    print(r.content)
    return render(request, "PaginaEjemplo/pagina_con_http.html", {"Palabras": r.content})