from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .forms import UserChangeForm
from .forms import UserCreationForm
from .models import ExtUser


class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = [
        'email',
        'firstname',
        'lastname',
        'is_admin',
        'is_superuser',
    ]

    list_filter = ('is_admin','is_superuser')

    fieldsets = (
                (None, {'fields': ('email', 'password', 'myURL')}),
                ('Personal info', {
                 'fields': (
                     'firstname',
                     'lastname',
                     'name_comp',
                     'phone',
                     'day_licenz'
                 )}),
                ('Permissions', {'fields': ('is_admin','is_superuser')}),
                ('Important dates', {'fields': ('last_login',)}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

# Регистрация нашей модели
admin.site.register(ExtUser, UserAdmin)
admin.site.unregister(Group)
