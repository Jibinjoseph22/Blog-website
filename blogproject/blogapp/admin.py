from django.contrib import admin
from .models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at', 'updated_at', 'content')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(status='publish')
        return qs

    def has_add_permission(self, request):
        # Restrict non-superusers from adding new blogs
        if not request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        # Restrict non-superusers from deleting blogs
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)
