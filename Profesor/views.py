from django.shortcuts import render
from Profesor.models import Profesor
from Profesor.forms import ProfesorFormulario

def crear_profesor(request):
    if request.method == 'GET':
        context = {
            'form': ProfesorFormulario()
        }
        return render(request,'crear_profesores.html',context=context)

    elif request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            Profesor.objects.create(
                nombre  = form.cleaned_data['nombre'], 
                edad    = form.cleaned_data['edad'], 
                sexo    = form.cleaned_data['sexo'], 
                correo  = form.cleaned_data['correo'],
                celular = form.cleaned_data['celular'], 
                tipo    = form.cleaned_data['tipo']
            )
            context = {
                'mensaje': 'Se registro el Profesor correctamente'
            }
        else:
            context = {
                'form_errores': form.errors,
                'form' : ProfesorFormulario()
            }
        return render(request,'crear_profesores.html',context=context)

def listar_profesor(request):
    if 'search' in request.GET:
        filtro = request.GET['search']
        profesores = Profesor.objects.filter(nombre__contains=filtro)
    else:
        profesores = Profesor.objects.all()

    context = {
                'profesores' : profesores
            }
    return render(request,'listar_profesores.html',context=context)

def editar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'form': ProfesorFormulario(
                        initial= {
                            'nombre' : profesor.nombre, 
                            'edad'   : profesor.edad,
                            'sexo'   : profesor.sexo,
                            'correo' : profesor.correo,
                            'celular': profesor.celular,
                            'tipo'   : profesor.tipo
                        }
                    )
        }
        return render(request,'editar_profesores.html',context=context)

    elif request.method == 'POST':
        form = ProfesorFormulario(request.POST)
        if form.is_valid():
            profesor.nombre=form.cleaned_data['nombre'] 
            profesor.edad=form.cleaned_data['edad']
            profesor.sexo = form.cleaned_data['sexo']
            profesor.correo=form.cleaned_data['correo']
            profesor.celular=form.cleaned_data['celular']
            profesor.tipo=form.cleaned_data['tipo']
            profesor.save()
            context = {
                'mensaje': 'Se Edito el Profesor correctamente'
            }
        else:
            context = {
                'form_errores': form.errors,
                'form' : ProfesorFormulario()
            }
        return render(request,'editar_profesores.html',context=context)

def eliminar_profesor(request, id):
    profesor = Profesor.objects.get(id=id)

    if request.method == 'GET':
        context = {
            'nombre': profesor.nombre
        }
        return render(request,'eliminar_profesores.html',context=context)
    else:
        profesor.delete()
        profesores = Profesor.objects.all()
        context = {
            'profesores': profesores
        }
        return render(request,'listar_profesores.html',context=context)
