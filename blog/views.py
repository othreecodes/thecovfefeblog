from django.shortcuts import render
from django.views.generic.detail import DetailView

from .models import Post, Category
# Create your views here.
from django.views.generic import ListView
from django.views.generic.base import TemplateView


def index(request):
    return render(request, 'blog/index.html')

def category(request):
    return None
# class-based views
class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'

class PostDetail(DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post'
