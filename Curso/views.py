from django.shortcuts import render
from Curso.models import Curso
from Curso.forms import CursoFormulario

def crear_curso(request):
    if request.method == 'GET':
        context = {
            'form': CursoFormulario()
        }
        return render(request,'crear_cursos.html',context=context)

    elif request.method == 'POST':
        form = CursoFormulario(request.POST)
        if form.is_valid():
            Curso.objects.create(
                nombre  = form.cleaned_data['nombre'], 
                creditos= form.cleaned_data['creditos'], 
                ciclo   = form.cleaned_data['ciclo'], 
                
            )
            context = {
                'mensaje': 'Se registro el Curso correctamente'
            }
        else:
            context = {
                'form_errores': form.errors,
                'form' : CursoFormulario()
            }
        return render(request,'crear_cursos.html',context=context)

def listar_curso(request):
    if 'search' in request.GET:
        filtro = request.GET['search']
        cursos = Curso.objects.filter(nombre__contains=filtro)
    else:
        cursos = Curso.objects.all()

    context = {
                'cursos' : cursos
            }
    return render(request,'listar_cursos.html',context=context)
