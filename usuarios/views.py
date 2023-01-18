from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User 
from usuarios.form import RegisterForm, UpdateForm, UserProfileForm
from usuarios.models import UserProfile

def login_view(request):
    if request.method == 'GET':
        form = AuthenticationForm()
        context = {
            'form' : form
        }
        return render(request, 'login.html',context=context)

    elif request.method == 'POST':
        form = AuthenticationForm(request=request, data = request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            user = authenticate(username = username, password = password)

            if user is not None:
                login(request, user)
                context = {'mensaje': f'Bienvenido {username}'}
                return render(request,'inicio.html',context)
            else:
                form = AuthenticationForm()   
                context={'errors': 'Usuario o contraseña incorrectos'}
                return render(request,'inicio.html',context)
        else:
            form = AuthenticationForm()   
            context={'errors': 'Usuario o contraseña incorrectos'}
            return render(request,'inicio.html',context)

def register(request):
    if request.method == 'GET':
        #form = UserCreationForm()
        form = RegisterForm()
        context = {
            'form' : form
        }
        return render(request, 'registro.html',context=context)

    elif request.method == 'POST':
        #form = UserCreationForm(request.POST)
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            return redirect('login')
        else:   
            context={
                'errors': form.errors,
                'form': RegisterForm()
            }
            return render(request, 'registro.html',context=context)

@login_required
def update_user(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'form': UpdateForm(
                        initial= {
                            'username'    : user.username, 
                            'first_name'  : user.first_name,
                            'last_name'   : user.last_name
                        }
                    )
        }
        return render(request, 'update_user.html',context=context)    

    elif request.method == 'POST':
        form = UpdateForm(request.POST)
        if form.is_valid():
            #user.username = form.cleaned_data['username']
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            context={'mensaje':'Se actualizo correctamente'}
            return render(request, 'update_user.html',context=context)
        else:   
            context={
                'errors': form.errors,
                'form': UpdateForm()
            }
            return render(request, 'update_user.html',context=context)

def editar_perfil(request):
    user = request.user
    if request.method == 'GET':
        context = {
            'form': UserProfileForm(
                        initial= {
                            'telefono'  : user.profile.telefono,
                            'fecha_nacimiento' : user.profile.fecha_nacimiento,
                            'foto'      : user.profile.foto
                        }
                    )
        }
        return render(request,'editar_perfiles.html',context=context)

    elif request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES)
        if form.is_valid():
            user.profile.telefono    = form.cleaned_data['telefono']
            user.profile.fecha_nacimiento = form.cleaned_data['fecha_nacimiento']
            user.profile.foto        = form.cleaned_data['foto']
            user.profile.save()

            context = {'mensaje': 'Se actualizo el Perfil correctamente'}
            return render(request,'editar_perfiles.html',context=context)
        else:
            context = {
                'form_errores': form.errors,
                'form' : UserProfileForm()
            }
        return render(request,'editar_perfiles.html',context=context)