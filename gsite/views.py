from django.conf import settings
from django.shortcuts import redirect, render

from gsite.models import BlogPost

def index(request):
    context = {'active_tab': 'home'}

    if request.headers.get('HX-Request'):  
        return render(request, 'gsite/_home.html', context)

    return render(
        request, "gsite/index.html", context
        )

def cli(request):
    context = {'active_tab': 'cli'}

    return render(
        request, "gsite/_cli.html", context
        )

def web(request):
    context = {'active_tab': 'web'}

    return render(
        request, "gsite/_web.html", context,
        )

def blog(request):
    posts = BlogPost.objects.all()

    context = {'active_tab': 'blog', 'posts': posts}

    return render(
        request, "gsite/_blog.html", context,
        )

def terms(request):
    return render(
        request, "gsite/terms.html"
        )

def privacy(request):
    return render(
        request, "gsite/privacy.html"
        )

def image_redirect(request, path):
    if settings.USE_S3:
        s3_url = f"https://{settings.AWS_S3_CUSTOM_DOMAIN}/images/{path}"
        return redirect(s3_url)
    else:
        return redirect(f"{settings.STATIC_URL}images/{path}")
