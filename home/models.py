from django.db import models
from django.template.defaultfilters import slugify

class Products(models.Model):
	title = models.TextField()
	description = models.TextField()
	price = models.TextField()
	quantity = models.IntegerField() 
	image = models.ImageField(upload_to='media')
	slug = models.CharField(max_length=100, null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.title)
		return super().save(*args, **kwargs )

