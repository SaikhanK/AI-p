from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.viewsets import GenericViewSet

class TestViewSet(GenericViewSet):

    def product_test(self, request: Request) -> Response:
        raise ValueError(request.POST)
        return Response({
            'test': 'hi'
        })