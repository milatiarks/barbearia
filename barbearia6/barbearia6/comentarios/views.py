# comentarios/views.py
from django.shortcuts import render, redirect
from .models import Feedback, Informacoes
from .forms import FeedbackForm

def home(request):
    informacoes = Informacoes.objects.all()
    return render(request, 'home.html', {'informacoes': informacoes})

def feedback_list(request):
    feedbacks = Feedback.objects.all()
    return render(request, 'comentarios/feedback_list.html', {'feedbacks': feedbacks})

def add_feedback(request):
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/feedback_list/')
    else:
        form = FeedbackForm()
    return render(request, 'comentarios/add_feedback.html', {'form': form})
