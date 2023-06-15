from django.shortcuts import render
from . import forms
from . import models
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy

def index(request):
    return render (request, "post/index.html")

class AnuncioCrear(CreateView):
    model = models.Post
    form_class = forms.PostForm
    template_name = "post/crear-anuncio.html"
    success_url = reverse_lazy("post:index")

class AnuncioLista(ListView):
    model = models.Post
    template_name = "post/lista-anuncios.html"
    context_object_name = "lista_anuncios"

class AnuncioBorrar(DeleteView):
    model = models.Post    




