from django.db import models

# Create your models here.
class Blog(models.Model):
    text = models.TextField()
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/',blank=True , null=True)
    date = models.DateTimeField(auto_now_add=True, blank=True , null=True)
    def __str__(self):
        return self.title