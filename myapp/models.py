from django.db import models

# Create your models here.
class Image(models.Model):
    image = models.ImageField(upload_to="images")  
    caption = models.CharField(max_length=200)  
    date = models.DateTimeField(auto_now_add=True)
  
    def __str__(self):  
        return self.caption  