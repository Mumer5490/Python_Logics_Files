from django.db import models

# Create your models here.

class cat_dog(models.Model):
    name = models.CharField(max_length=50 , blank=True, null= True)
    cat_dog_Img = models.ImageField(upload_to='images/', blank=True, null= True)

