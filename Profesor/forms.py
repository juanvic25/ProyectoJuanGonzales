from django import forms

class ProfesorFormulario(forms.Form):
    generos = (
        ('Masculino','Masculino'),('Femenino','Femenino')
    )
    contrato = (
        ('Contrato','Contrato'),('Nombrado','Nombrado')
    )
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=generos, required=True)
    correo = forms.EmailField()
    celular = forms.IntegerField()
    tipo = forms.ChoiceField(choices=contrato, required=True)