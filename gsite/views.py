from django.conf import settings
from django.shortcuts import render

def index(request):
    if request.headers.get('HX-Request'):  
        return render(request, 'gsite/_home.html')

    return render(
        request, "gsite/index.html",
        )

def cli(request):
    return render(
        request, "gsite/_cli.html",
        )

def web(request):
    return render(
        request, "gsite/_web.html",
        )

def blog(request):
    return render(
        request, "gsite/_blog.html",
        )