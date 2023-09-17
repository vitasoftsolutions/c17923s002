from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from .models import Employee, PhoneNumber
from .forms import UserChangeForm, UserCreationForm

class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'is_admin','is_staff','first_name','last_name','status','joined_date')
    list_filter = ('is_admin',)
    fieldsets = (
        (None, {'fields': ('email', 'password','first_name','last_name','username','phone_number','status','joined_date')}),
        ('Permissions', {'fields': ('is_admin','is_staff',)}),
        ('Verifications', {'fields': ('is_verified',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()

admin.site.register(Employee, UserAdmin)
admin.site.register(PhoneNumber)
#admin.site.unregister(Group)
