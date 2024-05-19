from django.db import models
from sorl.thumbnail import ImageField
# Create your models here.
class Post(models.Model):
    text=models.CharField(max_length=150,null=False,blank=False)
    matter=models.TextField()
    image=ImageField()
    def __str__(self):
        return self.text