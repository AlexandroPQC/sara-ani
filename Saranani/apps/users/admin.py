from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import User

class UserAdmin(UserAdmin):
    fieldsets = (
        ('User', {'fields' : ('username', 'password')}),
        ('Personal Information', {'fields': ('first_name',
                                            'last_name',
                                            'email',
                                            'nit',
                                            'birthday',
                                            'avatar')}),
        ('Permissions', {'fields': ('is_active',
                                    'is_staff',
                                    'is_superuser',
                                    'groups',
                                    'user_permissions')}),
    )

admin.site.register(User, UserAdmin)
