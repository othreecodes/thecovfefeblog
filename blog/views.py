from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .forms import UserForm
from .models import Post, Category
from django.shortcuts import *
from django.views.generic import ListView
from django.views.generic.base import TemplateView
from django.contrib.auth.forms import UserCreationForm


def index(request):
    return render(request, 'blog/index.html')


def category(request, category):
    # TODO:
    return HttpResponse(category)


# class-based views
class IndexView(ListView):
    template_name = 'blog/index.html'
    model = Post
    context_object_name = 'posts'


class PostDetail(DetailView):
    template_name = 'blog/post.html'
    model = Post
    context_object_name = 'post'


class UserCreate(CreateView):
    template_name = 'blog/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('blog:login')


from django.views.generic import View


class LoginView(View):
    def get(self, request):
        return render(request, 'blog/login.html')

    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        print("here")
        if user is not None:
            if user.is_active:
                login(request, user)
                print('jhjhh')
                return HttpResponseRedirect('/')
            else:
                return HttpResponse("Inactive user.")
        else:
            context = {"error": True}
            return render(request, 'blog/login.html', context=context)


class LogoutView(View):
    def get(self, request):
        logout(request)
        return reverse('blog:index')
