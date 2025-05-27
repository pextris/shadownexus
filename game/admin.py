from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomUser, Player, Enemy, Post

class CustomUserAdmin(BaseUserAdmin):
    model = CustomUser
    list_display = ("email", "handle", "faction", "is_staff", "is_superuser")
    search_fields = ("email", "handle")
    ordering = ("email",)
    fieldsets = (
        (None, {"fields": ("email", "password")}),
        ("Personal info", {"fields": ("handle", "faction")}),
        ("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": ("email", "password1", "password2", "handle", "faction", "is_staff", "is_superuser"),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Player)
admin.site.register(Enemy)
admin.site.register(Post)
