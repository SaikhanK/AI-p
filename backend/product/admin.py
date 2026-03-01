from django.contrib import admin
from .models import Product, ProductImage, Category, Attribute, AttributeValue, ProductAttribute

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Attribute)
admin.site.register(AttributeValue)
admin.site.register(ProductAttribute)