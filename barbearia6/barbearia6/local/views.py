from django.shortcuts import render

# Create your views here.

def local(request):
    return render(
        request,
        'local/local.html'
    )