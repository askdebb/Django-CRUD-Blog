from dataclasses import field
from msilib.schema import ListView
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Post
from django.views.generic import CreateView, ListView, UpdateView, DetailView, DeleteView

#Create Post Class Views
class PostListView(ListView):
    model = Post

class PostCreateView(CreateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")

class PostDetailView(DetailView):
    model = Post

class PostUpdateView(UpdateView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")

class PostDeleteView(DeleteView):
    model = Post
    fields = "__all__"
    success_url: reverse_lazy("blog:all")
