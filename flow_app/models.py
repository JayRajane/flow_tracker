# Create your models here.
from django.db import models
from django.utils import timezone

class FlowData(models.Model):
    date = models.DateField(default=timezone.now)
    time = models.TimeField(default=timezone.now)
    day = models.CharField(max_length=10)
    daily_flow = models.IntegerField()
    total_flow = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.date} - Daily: {self.daily_flow}, Total: {self.total_flow}"