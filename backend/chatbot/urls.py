from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .view import ConversationCreateView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("conversation/", ConversationCreateView.as_view(), name="conversation-create"),
]