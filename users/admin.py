from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreateForm, CustomUserChangeForm, CandidateCreateForm, CandidateChangeForm
from .models import CustomUser, Candidate


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreateForm
    form = CustomUserChangeForm
    model = CustomUser
    list_filter = ('is_staff',)
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        ('Informações de acesso', {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )



@admin.register(Candidate)
class CandidateAdmin(UserAdmin):
    add_form = CandidateCreateForm
    form = CandidateChangeForm
    model = Candidate
    list_display = ('first_name', 'last_name', 'email', 'is_staff')
    fieldsets = (
        ('Informações de acesso', {'fields': ('email', 'password')}),
        ('Informações pessoais', {'fields': ('first_name', 'last_name')}),
        ('Permissões', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Datas importantes', {'fields': ('last_login', 'date_joined')}),
    )