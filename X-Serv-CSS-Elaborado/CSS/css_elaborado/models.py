from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Pages (models.Model):
	name = models.TextField()
	content = models.TextField()
	def __unicode__(self):
		return self.name
