from django.db import models
from ..product.models import Product

class Conversation(models.Model):
    session_id = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add = True)

class Message(models.Model):
    ROLE_CHOICES = [
        ('user', 'User'),
        ('assistant', 'Assistant'),
        ('tool', 'Tool/System'),
    ]
    conversation = models.ForeignKey(Conversation, on_delete = models.CASCADE, related_name='messages')
    session_id = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)

class OfferRequest(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Entwurf'),
        ('sent', 'Gesendet'),
        ('accepted', 'Angenommen'),
    ]
    conversation = models.OneToOneField(Conversation, on_delete=models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    pdf_document = models.FileField(upload_to='offers/', null=True, blank=True)

class OfferItem(models.Model):
    offer_request = models.ForeignKey(OfferRequest, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField()
    unit_price_at_time = models.DecimalField(max_digits=10, decimal_places=2)