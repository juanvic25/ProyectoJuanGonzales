from django import forms
from Alumno.models import Alumno
class AlumnoFormulario(forms.Form):
    generos = (
        ('Masculino','Masculino'),('Femenino','Femenino')
    )
    nombre = forms.CharField(max_length=100)
    edad = forms.IntegerField()
    sexo = forms.ChoiceField(choices=generos, required=True)
    correo = forms.EmailField()

#class AlumnoFormulario(forms.ModelForm):
#    class Meta:
#        model = Alumno
#        fields = '__all__'