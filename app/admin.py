from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Post
from django.utils.html import format_html

class CustomUserAdmin(UserAdmin):
    list_display = ("username", "email", "phone", "is_staff", "is_superuser")

    fieldsets = list(UserAdmin.fieldsets) + [(
        "Extra Info", {"fields":("phone",)}
    )]

    add_fieldsets = list(UserAdmin.add_fieldsets) + [(
        "Extra Info", {"fields":("phone",)}
    )]



class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "user", "created_at", "image_path")
    search_fields = ("title", "contents")
    list_filter = ("created_at", "user")
    ordering = ["-created_at"]

    @admin.display(description="Image")
    def image_path(self, obj):
        if obj.image:
            return format_html(
                "<img src={} width='50px' height='50px'>",
                obj.image.url
            )
        return "No image"


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Post, PostAdmin)
