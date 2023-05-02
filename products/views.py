from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView

from products.forms import SignUpForm
from products.models import Items


# Create your views here.
class HomeView(ListView):
    model = Items
    template_name = "home.html"
    success_url = reverse_lazy("home")
    context_object_name = "items"


def products(requests):
    return render(requests, "products.html")


class UserCreateView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)