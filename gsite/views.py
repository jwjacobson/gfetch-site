from django.conf import settings
from django.shortcuts import render

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
    context = {'active_tab': 'blog'}

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