from rest_framework import viewsets
from .models import Product, productImage
from .serializers import ProductSerializer, ProductImageSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = productImage.objects.all()
    serializer_class = ProductImageSerializer
