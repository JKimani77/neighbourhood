from hdapp.forms import NeighbourhoodForm
from django.contrib import admin
from django.contrib.auth.forms import UserChangeForm
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from .models import User
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    fieldsets = (
        (None, {'fields': ('email', 'password' )}),
        (_('Personal info'), {'fields': ('first_name', 'last_name')}),
        (_('Permissions'), {'fields': ('is_active', 'is_staff', 'is_superuser','groups', 'user_permissions')}),
        (_('user_info'), {'fields': ('native_name')}),
        )
    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'password1', 'password2'),
            }),
            )
    list_display = ['email', 'first_name', 'last_name', 'is_staff', "native_name"]
    search_fields = ('email', 'first_name', 'last_name')
    ordering = ('email', )
    admin.site.register(User, UserAdmin)


class NeighbourhoodAdmin(UserAdmin):
    form = NeighbourhoodForm
    fieldsets = (
        (None, {'fields': ('email', 'password' )}),
     )
