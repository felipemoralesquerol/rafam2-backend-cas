from django.db import models

# Create your models here.
class Config(models.Model):
    code = models.CharField(max_length=20)
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    value_default = models.CharField(max_length=500)
    value = models.CharField(max_length= 500)
    created_at = models.DateTimeField()
    last_modified = models.DateTimeField()
