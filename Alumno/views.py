from django.shortcuts import render
from Alumno.models import Alumno
from Alumno.forms import AlumnoFormulario

def crear_alumno(request):
    if request.method == 'GET':
        context = {
            'form': AlumnoFormulario()
        }
        return render(request,'crear_alumnos.html',context=context)

    elif request.method == 'POST':
        form = AlumnoFormulario(request.POST)
        if form.is_valid():
            Alumno.objects.create(
                nombre=form.cleaned_data['nombre'], 
                edad=form.cleaned_data['edad'], 
                sexo = form.cleaned_data['sexo'], 
                correo=form.cleaned_data['correo']
            )
            context = {
                'mensaje': 'Se registro el Alumno correctamente'
            }
        else:
            context = {
                'form_errores': form.errors,
                'form' : AlumnoFormulario()
            }
        return render(request,'crear_alumnos.html',context=context)

def listar_alumno(request):
    if 'search' in request.GET:
        filtro = request.GET['search']
        alumnos = Alumno.objects.filter(nombre__contains=filtro)
    else:
        alumnos = Alumno.objects.all()

    context = {
                'alumnos' : alumnos
            }
    return render(request,'listar_alumnos.html',context=context)
