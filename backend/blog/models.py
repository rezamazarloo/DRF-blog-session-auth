from django.db import models
from filer.fields.image import FilerImageField
from filer.models import Image
from utils.models import CreatedUpdatedFields

# Create your models here.
class Badge(models.Model):
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name

class Post(CreatedUpdatedFields, models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    isPublished = models.BooleanField(default=False, verbose_name="is published")
    publishedAt = models.DateTimeField(null=True, blank=True, default=None, verbose_name="Published at")
    indexImage = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL, related_name='index_image')
    badges = models.ManyToManyField(Badge)
    gallery = models.ManyToManyField(Image, through='ImageGallery')
    def __str__(self):
        return self.title

class ImageGallery(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = FilerImageField(on_delete=models.CASCADE)
