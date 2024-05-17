from django.db import models

class Image(models.Model):
    objects = None
    photo=models.ImageField(upload_to="myimage")
    date=models.DateTimeField(auto_now_add=True)
