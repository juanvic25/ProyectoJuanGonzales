from django import forms

class CursoFormulario(forms.Form):
    nombre = forms.CharField(max_length=100)
    creditos = forms.IntegerField()
    ciclo = forms.IntegerField()
