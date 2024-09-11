from django.shortcuts import render

# Create your views here.

def horarios(request):
    return render(
        request,
        'horarios/horarios.html'
    )