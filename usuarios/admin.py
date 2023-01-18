from django.contrib import admin
from usuarios.models import UserProfile

@admin.register(UserProfile)
class UserAdmin(admin.ModelAdmin): 
    list_display = ('user',)