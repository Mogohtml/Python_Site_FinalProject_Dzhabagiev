from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.models import User


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ('email', 'first_name', 'last_name', 'status')
    search_fields = ('email', 'first_name', 'last_name')
    list_filter = ('status',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'phone', 'address')}),
        ('Permissions', {'fields': ('status', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone', 'address', 'status',
                       'is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
    )

    ordering = ('email',)

admin.site.register(User, CustomUserAdmin)

