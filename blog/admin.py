from django.contrib import admin
from blog.models import Blog

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'slug', 'body', 'is_published')
    list_filter = ('is_published',)
