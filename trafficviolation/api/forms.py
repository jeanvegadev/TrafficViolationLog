from django import forms


class InfraccionForm(forms.Form):
    placa_patente = forms.CharField(max_length=6)
    timestamp = forms.DateTimeField()
    comentarios = forms.CharField(max_length=1000)
    token = forms.CharField(max_length=50)


class GenerarInformeForm(forms.Form):
    email = forms.EmailField()


class OficialForm(forms.Form):
    nombre = forms.CharField(max_length=100)
    numero_unico = forms.CharField(max_length=50)
