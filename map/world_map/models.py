from django.db import models


class Coordinats(models.Model):
    pointer = models.TextField(max_length=255) 