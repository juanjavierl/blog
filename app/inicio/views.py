from django.shortcuts import render, redirect

from .forms import *
# Create your views here.
def inicio(request):

    return render(request, 'base.html')



def login(request):
    #print("Tipo de la peticion: ", request.method)
    if request.method == 'POST':
        formulario = NameForm(data = request.POST)
        if formulario.is_valid():
            return redirect("/logueado/")

        #print(request.POST['nombre'])
    else:
        formulario = NameForm()
    return render(request, 'login.html',{'formulario':formulario})


def detalleUser(request):
    nombre = "administrador"

    
    return render(request, 'detalleUser.html',{'nombre':nombre})