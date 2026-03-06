from rest_framework import serializers
from .models import Product, ProductImage
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductSerializer(serializers.Serializer):
    category = serializers.ListField(required=False)
    brand = serializers.ListField(required=False)
    attribute = serializers.ListField(required=False)
    attribute_value = serializers.DictField(required=False)
    data = serializers.ListField(required=False)
    
    class Meta:
        add_custom_attributes = True
        add_grouping_fields = False