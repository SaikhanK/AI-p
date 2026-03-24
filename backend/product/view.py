from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer, ProductDetailSerializer
from .paramter import QueryParameter
from .services.querying import generate_dataframe
from .services.category_service import get_categories
from .services.brand_service import get_brands
from .services.response_service import generate_response
import pandas as pd

class ProductView(GenericViewSet):

    def getProducts(self, request: Request) -> Response:
        serializer_class = ProductSerializer
        categories = get_categories()
        brands = get_brands()
        data = QueryParameter.model_validate(dict(request.query_params.items()))
        df = generate_dataframe(data)
        records = df.to_dict(orient="records")
        return generate_response(serializer_class, records, brands, categories)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
