from django.db import models

from core.models import Pharmaceutical


class Drug(models.Model):
    name = models.CharField(max_length=255)
    pharmaceutical = models.ForeignKey(
        Pharmaceutical, null=True, blank=True, on_delete=models.SET_NULL)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
