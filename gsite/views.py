from django.conf import settings
from django.shortcuts import render

def index(request):
    if request.headers.get('HX-Request'):  
        return render(request, 'gsite/_home.html')

    return render(
        request, "gsite/index.html",
        )
