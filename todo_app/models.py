from django.db import models

class items(models.Model):
    title = models.CharField(max_length = 25)
    description = models.CharField(max_length = 250)
    checked = models.BooleanField(default=False, blank=True)
