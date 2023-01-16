from django.urls import path

from Alumno.views import alumnoListView, alumnoCreateView, alumnoDeleteView, alumnoUpdateView

urlpatterns = [
   path('crear-alumno/',alumnoCreateView.as_view() ),
   path('listar-alumno/',alumnoListView.as_view()),
   path('editar-alumno/<int:pk>/',alumnoUpdateView.as_view()),
   path('eliminar-alumno/<int:pk>/',alumnoDeleteView.as_view()),
]