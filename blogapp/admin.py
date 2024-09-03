from django.contrib import admin
from .models import Blog, Draft

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'status', 'created_at', 'updated_at', 'content')
    list_filter = ('status', 'category')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

    def get_queryset(self, request):
        # Optionally, filter out drafts from the default admin view if needed
        qs = super().get_queryset(request)
        if not request.user.is_superuser:
            qs = qs.filter(status='published')
        return qs

    def has_add_permission(self, request):
        # Restrict non-superusers from adding new blogs
        if not request.user.is_superuser:
            return False
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        # Restrict non-superusers from editing drafts
        if obj and obj.status == 'draft' and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Restrict non-superusers from deleting blogs
        if not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)

# Register the Draft model in admin
@admin.register(Draft)
class DraftAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'created_at')
    list_filter = ('category', 'author')
    search_fields = ('title', 'content')
    ordering = ('-created_at',)

    def has_add_permission(self, request):
        # Allow adding drafts by any logged-in user
        return super().has_add_permission(request)

    def has_change_permission(self, request, obj=None):
        # Allow editing drafts by the author or superusers
        if obj and obj.author != request.user and not request.user.is_superuser:
            return False
        return super().has_change_permission(request, obj)

    def has_delete_permission(self, request, obj=None):
        # Allow deleting drafts by the author or superusers
        if obj and obj.author != request.user and not request.user.is_superuser:
            return False
        return super().has_delete_permission(request, obj)
