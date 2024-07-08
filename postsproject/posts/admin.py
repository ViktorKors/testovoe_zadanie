from django.contrib import admin

from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    Админка для модели Post.
    """

    list_display = ("id", "title", "content", "created_at", "updated_at")
    list_editable = ("title", "content")
    search_fields = ("title", "content")
    list_filter = ("created_at", "updated_at")
    readonly_fields = ("created_at", "updated_at")
    ordering = ("-created_at",)
