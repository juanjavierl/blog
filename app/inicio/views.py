from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required

from .models import *
from .forms import *
# Create your views here.

def loguearse(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username,password=password)
            print(user)
            if user is not None:
                print("TE AUTENTICASTE EN EL SISTEMA")
                login(request, user)
                return redirect("/inicio")
            else:
                messages.error(request,'Error, Contactese con el administrador para resolver el problema gracias.')
            return redirect('/')
        else:
            messages.error(request,'Error, datos incorrectos intente nuevamente gracias.')
        return redirect('/login')
    else:
        form = AuthenticationForm()
        contexto = {'form':form}
    return render(request, 'login.html', contexto)


@login_required(login_url="/")
def inicio(request):

    return render(request,'base.html')

def cerrarSesion(request):
    logout(request)

    return redirect("/")

def contacto(request):
    #print("Tipo de la peticion: ", request.method)
    if request.method == 'POST':
        formulario = NameForm(data = request.POST)
        if formulario.is_valid():
            return redirect("/logueado/")

        #print(request.POST['nombre'])
    else:
        formulario = NameForm()
    return render(request, 'contacto.html',{'formulario':formulario})


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



@login_required(login_url="/")
def listarProductos(request):
    productos = Producto.objects.all()
    usuario = request.user.first_name.upper() +" "+ request.user.last_name
    print(usuario)
    datos = {
        'productos':productos
    }
    return render(request, 'listarProductos.html', datos)


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            messages.success(request, f'Usuario {username} creado exitosamente')
            return redirect("/register/")
    else:
        form = UserRegisterForm()
    
    contexto = {'form':form}
    return render(request,'register.html',contexto)
