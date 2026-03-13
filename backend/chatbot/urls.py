from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf import settings
from django.conf.urls.static import static
from .view import ModelView

urlpatterns = [
    path("llm/", ModelView.as_view({'get': 'chat_with_agent'}), name="llm")
]