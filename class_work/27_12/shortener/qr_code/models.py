# qr_code/models.py
from django.db import models
from links.models import Link

class QRCode(models.Model):
    link = models.OneToOneField(Link, on_delete=models.CASCADE, related_name='qr_code')
    image = models.ImageField(upload_to='qr_codes/')
    created_at = models.DateTimeField(auto_now_add=True)
