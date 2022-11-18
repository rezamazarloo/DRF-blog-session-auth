from django.db import models
from filer.fields.image import FilerImageField
from filer.models import Image

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=50)

class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    isPublished = models.BooleanField()
    createdAt = models.DateTimeField()
    updatedAt = models.DateTimeField()
    publishedAt = models.DateTimeField()
    indexImage = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='index_image')
    badges = models.ManyToManyField(Badge)
    gallery = models.ManyToManyField(Image, through='ImageGallery')

class ImageGallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = FilerImageField(on_delete=models.CASCADE)
