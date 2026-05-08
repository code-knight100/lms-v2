from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class UserAdminCustom(UserAdmin):
    list_display = ["id", "username", "email", "role","first_name", "last_name", "gender", "address", "phone_no", "photo", "is_active", "is_staff", "is_superuser"]
    list_display_links = ["id", "username"]
    list_editable = ["is_active", "is_staff", "is_superuser"]
    list_filter = ["role", "gender", "is_active", "is_staff", "is_superuser"]
    search_fields = ["username", "first_name", "last_name"]
    list_per_page = 10
    
    fieldsets = (
        ( ("Credentials"), {"fields":("username", "password")} ),
        ( ("Personal Info"), {"fields": ("first_name", "last_name", "email")}),
        (("Profile"), {"fields": ("phone_no", "address", "photo", "gender", "role")}),
        (("Permissions"), {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        (("Important Dates"), {"fields":("last_login", "date_joined")})  # cM*  - use the fields name as it is
    )