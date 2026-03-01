from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from .models import Conversation

class ConversationCreateView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        if not request.session.session_key:
            request.session.create()

        conversation, created = Conversation.objects.get_or_create(
            session_id=request.session.session_key,
            is_active=True
        )

        return Response({
            "conversation_id": conversation.id,
        })
