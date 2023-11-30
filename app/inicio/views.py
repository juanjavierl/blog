from django.shortcuts import render, redirect

from .models import *
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


def crear_categoria(request):
    if request.method == 'POST':
        formulario = CategoriaForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("/ver_categorias/")
    else:
        formulario = CategoriaForm()
    return render(request,'crear_categoria.html',{'formulario':formulario})

def ver_categorias(request):
    categorias = Categoria.objects.all()

    return render(request, 'ver_categorias.html',{'categorias':categorias})


def crear_producto(request):
    if request.method == 'POST':
        formulario = ProductoForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect("/listar_productos/")
    else:
        formulario = ProductoForm()
    return render(request, 'crear_producto.html',{'formulario':formulario})


def listarProductos(request):
    productos = Producto.objects.all()
    datos = {
        'productos':productos
    }
    return render(request, 'listarProductos.html', datos)