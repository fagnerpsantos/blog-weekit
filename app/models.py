from django.db import models

# Create your models here.

class Post(models.Model):
    titulo = models.CharField(max_length=50, null=False, blank=False)
    descricao = models.CharField(max_length=200, null=False, blank=False)
    conteudo = models.TextField(null=False, blank=False)

class Comentario(models.Model):
    conteudo = models.TextField(null=False, blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)