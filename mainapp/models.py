from django.db import models

# Create your models here.

class About_us(models.Model):
    title = models.CharField(max_length=100,blank=False)  # A short text field for the title
    description = models.TextField(max_length=700, blank=False)  # A longer text field for the description
    image = models.ImageField(upload_to='media/banner_image')  # An image upload field

    def __str__(self):
        return self.title
