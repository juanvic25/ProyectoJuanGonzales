from django.shortcuts import render, redirect

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate

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
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(request, 'registro.html',context=context)

    elif request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:   
            context={
                'errors': form.errors,
                'form': UserCreationForm()
            }
            return render(request, 'registro.html',context=context)
            