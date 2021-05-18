from django.contrib.postgres.fields import ArrayField
from django.db import models
import uuid


class StatusChoice(models.TextChoices):
    INSERTED = 'inserted'
    CONSUMED = 'consumed'


class Workflow(models.Model):
    UUID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    status = models.CharField(max_length=8, choices=StatusChoice.choices, default='False', blank=True)
    data = models.JSONField()
    steps = ArrayField(base_field=models.CharField(max_length=200, null=True), default=list, blank=True)

