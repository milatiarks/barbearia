from django.contrib import admin
from .models import Feedback, Informacoes

# Register your models here.

@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'comentario')

@admin.register(Informacoes)
class InformacoesAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'imagem')
