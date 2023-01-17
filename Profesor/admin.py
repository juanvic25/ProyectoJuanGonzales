from django.contrib import admin

from Profesor.models import Profesor

#1ra forma para mostrar los modelos

@admin.register(Profesor)

class ProfesorAdmin(admin.ModelAdmin): 
    list_display = ('nombre','correo','tipo')
    search_fields = ('nombre',)
    list_filter = ('tipo',)
