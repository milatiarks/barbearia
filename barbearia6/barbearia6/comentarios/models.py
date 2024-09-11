from django.db import models

# Create your models here.

class Feedback(models.Model):
    nome = models.CharField(max_length=100)
    comentario = models.TextField()

    def __str__(self):
        return self.nome

class Informacoes(models.Model):
    descricao = models.TextField()
    imagem = models.ImageField(upload_to='imagens/')

    def __str__(self):
        return self.descricao
