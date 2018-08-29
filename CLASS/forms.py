from django import forms
from . models import *
class Contacto_form(forms.Form):
    correo = forms.EmailField(widget=forms.TextInput())
    asunto = forms.CharField(widget=forms.TextInput())
    texto = forms.CharField(widget=forms.TextInput())

#class login_form(forms.Form):
    #username = forms.CharField(widget=forms.TextInput())
    #password = forms.PasswordField(widget= forms.TextInput())

class agregar_producto_form(forms.ModelForm):
    class Meta:
        model = Producto
        fields = '__all__'
        #fields = ['nombre','marca'] para agregar en el formulario solo ciertos atributos
        