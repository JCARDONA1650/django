from django.db import models

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=250)
    contents = models.TextField()

    def __str__(self):  # agregado funcion
        return self.title
