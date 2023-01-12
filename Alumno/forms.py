from django import forms

class AlumnoFormulario(forms.Form):
    generos = (
        ('Masculino','Masculino'),('Femenino','Femenino')
    )
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    sexo = forms.CharField(max_length=50)
    sexo = forms.ChoiceField(choices=generos, required=True)
    correo = forms.EmailField()