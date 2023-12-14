from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import * #Categoria, Producto,,,

class NameForm(forms.Form):
    nombre = forms.CharField(label= "Ingrese su Nombre",help_text="Informacion requerida *",widget=forms.TextInput(attrs={
        'placeholder':'Escriba su nombre',
        'autocomplete':'off'
    }))

    Email = forms.EmailField(label= "Ingrse su correo", required = True)


    def clean_nombre(self):
        nombre = self.cleaned_data.get('nombre', None)
        print("Valor de atributo:", nombre)
        if nombre is not None:
            if nombre == 'maria':
                raise forms.ValidationError("Maria no es un nombre Permitido.")

        if len(nombre)>5:
            raise forms.ValidationError("El nombre no debe pasar mas de 5 letras")

        return nombre


tipo_persona = (
    ('Estudiante', 'Estudiante'),
    ('Maestro', 'Maestro'),
    ('Experimentado', 'Experimentado'),
)


class NameForm(forms.Form):
    nombre = forms.CharField(label= "Nombre",help_text="Informacion requerida *")
    mensaje = forms.CharField(label="Mensaje", help_text="Escriba su mensaje")
    Email = forms.EmailField(label= "Ingrse su correo", required = True)


class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria

        exclude=('estado',)



class ProductoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control','placeholder':'Nombre del Producto'
                }
        )
    )
    precio = forms.FloatField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control','placeholder':'Precio'
                }
        )
    )

    stock = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control','placeholder':'Precio'
                }
        )
    )
    
    class Meta:
        model = Producto

        exclude=('estado',)



class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Confirma Contraseña', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ['username', 'password1', 'password2', 'email', 'first_name', 'last_name']#AQUI PUEDES QUITAR O AUMENTAR LOS DEMAS ATRIBUTOS DE TIENE EN USUARIOS
		help_texts = {k:"" for k in fields }
    