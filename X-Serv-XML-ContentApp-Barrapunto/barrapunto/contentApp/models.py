from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Content(models.Model):
	name = models.CharField(max_length=50)
	content = models.TextField()