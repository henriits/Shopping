from django.urls import path
from .views import *

urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("products/", products, name="products"),
    path("accounts/signup/", UserCreateView.as_view(), name="signup"),
]