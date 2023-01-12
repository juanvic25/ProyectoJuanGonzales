from django.urls import path

from Alumno.views import crear_alumno, listar_alumno

urlpatterns = [
   path('crear-alumno/',crear_alumno),
   path('listar-alumno/',listar_alumno),
]