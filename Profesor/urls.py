from django.urls import path

from Profesor.views import crear_profesor, listar_profesor, editar_profesor, eliminar_profesor

urlpatterns = [
   path('crear-profesor/',crear_profesor),
   path('listar-profesor/',listar_profesor),
   path('editar-profesor/<int:id>/',editar_profesor),
   path('eliminar-profesor/<int:id>/',eliminar_profesor),
]