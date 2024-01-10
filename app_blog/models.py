from django.db import models

# Create your models here.

class Blog(models.Model):

    title = models.CharField(max_length = 200)
    image = models.ImageField(upload_to='images/')
    description = models.TextField(null=True)

    def __str__(self):
        return self.title
