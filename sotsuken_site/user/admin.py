from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
class MyUserAdmin(UserAdmin):
    model = User
    #fieldsets = UserAdmin.fieldsets #+ ((None, {'fields': ('"anything"',)}),)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_admin', 'is_staff', 'is_superuser')}),
    )
    
    list_display = ['username', 'is_active']
 
 
admin.site.register(User, MyUserAdmin)
