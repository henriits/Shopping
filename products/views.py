from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from products.forms import SignUpForm
from products.models import Post


# Create your views here.
class HomeView(ListView):
    model = Post
    template_name = "home.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"


class ProductsView(ListView):
    model = Post
    template_name = "products.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"


class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ProductDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "detail.html"
    model = Post
