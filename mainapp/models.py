from django.db import models

# Create your models here.
# ============ banner section model==============================
class Banner(models.Model):
    title = models.CharField(max_length=100,blank=False)  # A short text field for the title
    description = models.TextField(max_length=700, blank=False)  # A longer text field for the description
    def __str__(self):
        return self.title
#=============service section model =======================
class Service_heading(models.Model):
    heading = models.CharField(max_length=100,default="Default Heading")
    def __str__(self):
        return self.heading
class Service(models.Model):
    service_headding = models.ForeignKey(Service_heading, on_delete=models.CASCADE, related_name="Service",null=True) 
    title = models.CharField(max_length=100,blank=False) 
    description = models.TextField(max_length=700, blank=False)
    def __str__(self):
        return self.title
class Cetagory(models.Model):
    service = models.ForeignKey(Service, on_delete=models.CASCADE, related_name="categorly")
    description = models.TextField(max_length=700, blank=False)
    def __str__(self):
        return str(self.service)
class S_post(models.Model):
    category = models.ForeignKey(Cetagory, on_delete=models.CASCADE, related_name="S_post")
    title = models.CharField(max_length=100,blank=False) 
    description = models.TextField(max_length=700, blank=False)
    image = models.ImageField(upload_to='post/image')
    def __str__(self):
        return self.title        
# ============ about section model===============================
class About_us(models.Model):
    title = models.CharField(max_length=100,blank=False)  # A short text field for the title
    description = models.TextField(max_length=700, blank=False)  # A longer text field for the description
    image = models.ImageField(upload_to='media/banner_image')  # An image upload field

    def __str__(self):
        return self.title
