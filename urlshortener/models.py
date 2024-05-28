from django.db import models

class Url(models.Model):
    original_url = models.CharField(max_length=600)
    shorten_url = models.CharField(max_length=8)
    creation_date = models.CharField(max_length=10)