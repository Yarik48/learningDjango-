from django.contrib.admin.helpers import AdminForm
from django.contrib.auth import login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView, DetailView
from pyexpat import model

from .models import *
from .forms import AddPostForm, RegisterUserForm, LoginUserForm, AddMessageForm
from .utils import DataMixin


def index(request):
    posts = Posts.objects.all()
    return render(request, 'posts/index.html', {'posts': posts})


class DetailPost(DetailView):
    model = Posts
    template_name = 'posts/show.html'
    context_object_name = 'post'

def show_day(request, day_id):
    posts = Posts.objects.filter(day=day_id)
    return render(request, 'posts/show_day.html', {'posts':posts})


def show_post(request, post_id):
    post = Posts.objects.get(id=post_id)
    return render(request, 'posts/show.html', {'post':post})


def show_obj(request, obj_id):
    posts = Posts.objects.filter(object=obj_id)
    return render(request, 'posts/show_obj.html', {'posts':posts, 'object':object})


def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AddPostForm()
    return render(request, 'posts/add_page.html', {'form': form})


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'posts/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация")
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('index')


class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'posts/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('index')


def logout_user(request):
    logout(request)
    return redirect('login')


def profile(request):
    return render(request, 'posts/profile.html')


class PostsUpdateView(UpdateView):
    model = Posts
    template_name = 'posts/update_page.html'

    form_class = AddPostForm



class AddMessage(View):
    def post(self, request, pk):
        form = AddMessageForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.object_id = pk
            form.save()
        return redirect(f'/chat/{pk}')


def chats(request):
    return render(request, 'posts/chats.html')

def show_chat(request, object_id):
    object = Object.objects.get(pk=object_id)
    return render(request, 'posts/show_chat.html', {'object': object})