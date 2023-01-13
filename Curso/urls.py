from django.urls import path

from Curso.views import crear_curso, listar_curso

urlpatterns = [
   path('crear-curso/',crear_curso),
   path('listar-curso/',listar_curso),
]