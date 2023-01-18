from django.urls import path
from django.contrib.auth.views import LogoutView
from usuarios.views import login_view, register, update_user, editar_perfil

urlpatterns = [
    path('login/',login_view, name='login'),
    path('logout/',LogoutView.as_view(template_name = 'logout.html')),
    path('register/',register),
    path('update/',update_user),
    path('editar_perfil/',editar_perfil),
]