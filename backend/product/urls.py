from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import ProductViewSet, ProductImageViewSet, ProductView
from .test_api import *
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"products", ProductViewSet, basename="products")
router.register(r"image", ProductImageViewSet, basename="images")

urlpatterns = [
    path('', include(router.urls)),
    path('test/', TestViewSet.as_view({'get': 'product_test'}), name="test_api"),
    path('product/', ProductView.as_view({'get': 'getProducts'}), name="product")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)