from django.db import models


class BlogPost(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_paragraphs(self):
        paragraphs = self.body.split('\n\n')
        return [p.strip() for p in paragraphs if p.strip()]