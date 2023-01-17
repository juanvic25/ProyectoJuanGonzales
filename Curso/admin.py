from django.contrib import admin

from Curso.models import Curso

#1ra forma para mostrar los modelos

@admin.register(Curso)

class CursoAdmin(admin.ModelAdmin): 
    list_display = ('nombre','creditos','ciclo')
    search_fields = ('nombre',)