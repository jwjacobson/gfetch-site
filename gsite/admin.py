from django.contrib import admin

from gsite.models import BlogPost

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ["title", "created_on"]
    search_fields = ("title", "body", "created_on")
