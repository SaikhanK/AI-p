from django.db import models

class Conversation(models.Model):
    session_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)

class Message(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE, related_name='messages')
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)