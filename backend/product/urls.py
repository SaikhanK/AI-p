from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import ProductViewSet, ProductImageViewSet
from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()
router.register(r"product", ProductViewSet, basename="products")
router.register(r"image", ProductImageViewSet, basename="images")

urlpatterns = [
    path('', include(router.urls))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)