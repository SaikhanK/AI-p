from rest_framework import serializers
from .models import Product, productImage

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = productImage
        fields = ["image"]

class ProductSerializer(serializers.ModelSerializer):
    images = ProductImageSerializer(many=True, read_only=True)
    class Meta:
        model = Product
        fields = ['id', 'title', 'price', 'images']