from django import forms

class NameForm(forms.Form):
    nombre = forms.CharField(label= "Ingrse su Nombre",help_text="Informacion requerida *",widget=forms.TextInput(attrs={
        'placeholder':'Escriba su nombre',
        'autocomplete':'off'
    }))

    Email = forms.EmailField(label= "Ingrse su correo")