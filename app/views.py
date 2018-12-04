from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def home(request):
    posts = Post.objects.all()
    return render(request, 'blog/index.html', {'posts':posts})

def show_post(request, id):
    post = Post.objects.get(id=id)
    comentarios = post.comentario_set.all()
    if request.method == "POST":
        form_comentario = ComentarioForm(request.POST)
        if form_comentario.is_valid():
            form = form_comentario.save(commit=False)
            form.post = post
            form.save()
    form_comentario = ComentarioForm()
    return render(request, 'blog/post.html', {'post':post, 'comentarios':comentarios, 'form_comentario':form_comentario})
