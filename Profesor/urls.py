from django.urls import path

from Profesor.views import crear_profesor, listar_profesor

urlpatterns = [
   path('crear-profesor/',crear_profesor),
   path('listar-profesor/',listar_profesor),
]