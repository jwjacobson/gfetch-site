from django.contrib import admin

from gsite.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on", "last_modified"]
    list_filter = ['created_on', 'last_modified']
    search_fields = ("title", "body")
    readonly_fields = ['created_on', 'last_modified']