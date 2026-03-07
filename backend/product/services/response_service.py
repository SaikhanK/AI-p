from typing import Hashable, Any, List
from ..serializers import ProductSerializer
from rest_framework.response import Response

def generate_response(serializer_class: ProductSerializer, records: list[dict[Hashable, Any]], brands: List, categories: List) -> Response:
    serializer_data = {

        "category": categories,
        "brand": brands,
        "data": records
    }
    serializer = serializer_class(data = serializer_data)
    serializer.is_valid(raise_exception=True)
    return Response(serializer.data)