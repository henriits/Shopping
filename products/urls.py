from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from shopping_paradise.views import HomeView, UserCreateView
from .views import *

app_name = "products"  # this will be used in links to define ex: products:details

urlpatterns = [
    path("",HomeView.as_view(), name="home"),
    path("products/", ProductsView.as_view(), name="products"),
    path("products/<int:pk>/", ProductDetailView.as_view(), name="detail")
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)