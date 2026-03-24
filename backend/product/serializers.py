from rest_framework import serializers
from .models import Product, ProductImage
from rest_framework import serializers

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ["image"]

class ProductDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ["title", "price"]

class ProductSerializer(serializers.Serializer):
    category = serializers.ListField(required=False)
    brand = serializers.ListField(required=False)
    attribute = serializers.ListField(required=False)
    attribute_value = serializers.DictField(required=False)
    data = serializers.ListField(required=False)
    
    class Meta:
        add_custom_attributes = True
        add_grouping_fields = False

class ProductChatSerializer(serializers.ModelSerializer):
    # Wir holen uns nur den Namen der Kategorie statt des ganzen Objekts
    category_name = serializers.ReadOnlyField(source='category.name')

    class Meta:
        model = Product
        # Nur die Felder, die du für den Einkaufswagen/Frontend wirklich brauchst
        fields = ["id", "title", "price", "category_name"]