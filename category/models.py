from django.db import models

# Create your models here.
class Category(models.Model):
  name = models.CharField(max_length=255)
  image = models.ImageField(upload_to = 'images/category', null= True)  
  image_url = models.TextField(null=True)
  is_activate = models.IntegerField(default=1)
  def __str__(self):
    return self.name