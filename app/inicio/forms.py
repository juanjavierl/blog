from django import forms

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
    mensaje = form.TextField(label="Mensaje", help_text="Escriba su mensaje")
    Email = forms.EmailField(label= "Ingrse su correo", required = True)
