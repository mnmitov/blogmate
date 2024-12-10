from django.contrib import admin
from account.models import AppUser, Profile

# Register your models here.

@admin.register(AppUser)
class AccountAdmin(admin.ModelAdmin):
    search_fields = ['email', 'username']
    list_display = ['email', 'username', 'last_login', 'is_superuser', 'is_staff', 'is_active']
    list_filter = ['email', 'username']
    list_per_page = 10
    ordering = ('-id',)
    list_display_links = ['email']


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name']
    list_display = ['first_name', 'last_name', 'age']
    list_display_links = ['first_name', 'last_name']
    ordering = ('first_name', 'last_name')
    list_per_page = 10
