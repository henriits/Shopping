from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView

from products.models import Post


# Create your views here.


class ProductsView(ListView):
    model = Post
    template_name = "products/products.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"


class AllProductsView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "products/allproducts.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"

    def get_queryset(self):
        queryset = super().get_queryset()
        query = self.request.GET.get('q')
        if query:
            queryset = queryset.filter(Q(title__icontains=query) | Q(text__icontains=query))
        return queryset


class ProductDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "products/detail.html"
    model = Post


class ShoppingCartView(ListView, LoginRequiredMixin):
    template_name = "products/shoppingcart.html"
    model = Post
