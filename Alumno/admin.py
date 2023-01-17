from django.contrib import admin

from Alumno.models import Alumno

#1ra forma para mostrar los modelos

@admin.register(Alumno)

class AlumnoAdmin(admin.ModelAdmin): 
    list_display = ('nombre','edad','sexo','correo')
    search_fields = ('nombre',)