from rest_framework.viewsets import GenericViewSet
from rest_framework import viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Product, ProductImage
from .serializers import ProductSerializer, ProductImageSerializer
from .paramter import QueryParameter
from .services.querying import generate_dataframe
from .services.category_service import get_categories
from .services.brand_service import get_brands
import pandas as pd

class ProductView(GenericViewSet):

    def getProducts(self, request: Request) -> Response:
        serializer_class = ProductSerializer
        categories = get_categories()
        brands = get_brands()
        data = QueryParameter.model_validate(dict(request.query_params.items()))
        df = generate_dataframe(data)
        records = df.to_dict(orient="records")
        serializer_data = {

            "category": categories,
            "brand": brands,
            "data": records
        }
        serializer = serializer_class(data = serializer_data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.data)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductImageViewSet(viewsets.ModelViewSet):
    queryset = ProductImage.objects.all()
    serializer_class = ProductImageSerializer
