from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from .paramter import QueryParameter
import pandas as pd

class ProductView(GenericViewSet):

    def getProducts(self, request: Request) -> Response:
        data = QueryParameter.model_validate(dict(request.query_params.items()))
        return Response

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
