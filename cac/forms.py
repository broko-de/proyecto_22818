from django import forms

class ContactoForm(forms.Form):
    nombre = forms.CharField(label='Nombre')
    email = forms.EmailField(label='Email',max_length=150)
    asunto = forms.CharField(label='Asunto',required=False)
    mensaje = forms.CharField(label='Mensaje',required=False)