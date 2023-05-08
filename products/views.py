
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView


from products.models import Post


# Create your views here.


class ProductsView(ListView):
    model = Post
    template_name = "products/products.html"
    success_url = reverse_lazy("home")
    context_object_name = "posts"




class ProductDetailView(DetailView):
    http_method_names = ["get"]
    template_name = "products/detail.html"
    model = Post
