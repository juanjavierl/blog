from django.shortcuts import render

from .forms import *
# Create your views here.
def inicio(request):

    return render(request, 'base.html')



def login(request):
    if request.method == 'POST':
        print(request.POST['nombre'])
    formulario = NameForm()
    return render(request, 'login.html',{'formulario':formulario})


def detalleUser(request):
    nombre = "administrador"

    
    return render(request, 'detalleUser.html',{'nombre':nombre})