from django.contrib import admin

# Register your models here.
from products.models import Post, Item

admin.site.register(Post)
admin.site.register(Item)

