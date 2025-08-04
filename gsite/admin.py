from django.contrib import admin
from markdownx.admin import MarkdownxModelAdmin

from gsite.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(MarkdownxModelAdmin):
    list_display = ["title", "created_on"]
    list_filter = ['created_on', 'last_updated']
    search_fields = ("title", "body", "created_on")
    readonly_fields = ['created_on', 'last_updated']