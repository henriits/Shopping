from django.urls import path
from .views import *

app_name = "products"  # this will be used in links to define ex: products:details

urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("products/", ProductsView.as_view(), name="products"),
    path("accounts/signup/", UserCreateView.as_view(), name="signup"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="detail")
]