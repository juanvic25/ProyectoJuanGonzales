from django.views.generic import ListView, CreateView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from Alumno.models import Alumno

class alumnoListView(LoginRequiredMixin, ListView):
    modelmodel = Alumno
    template_name = 'listar_alumnos.html'

    def get_queryset(self):
        filtro = self.request.GET.get('search')
        if filtro is not None:
            listado_filtrado = Alumno.objects.filter(nombre__contains = filtro)
        else:
            listado_filtrado = Alumno.objects.all
        return listado_filtrado
    
class alumnoCreateView(CreateView):
    model = Alumno
    template_name = 'crear_alumnos.html'
    fields = '__all__'
    success_url = '/alumno/listar-alumno/'

class alumnoDeleteView(DeleteView):
    model = Alumno
    template_name = 'listar_alumnos.html'
    success_url = '/alumno/listar-alumno/'

class alumnoUpdateView(UpdateView):
    model = Alumno
    fields = '__all__'
    template_name = 'editar_alumnos.html'
    success_url = '/alumno/listar-alumno/'