from django.contrib import admin
from .models import CustomUser, Product, ProductLike, Favorite

admin.site.register(CustomUser)

admin.site.register(Product)

admin.site.register(ProductLike)

admin.site.register(Favorite)
