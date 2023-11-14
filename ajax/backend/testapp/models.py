from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=1000)
    email = models.CharField(max_length=1000)
    bio = models.CharField(max_length=1000)
