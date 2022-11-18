from django.db import models
from django.contrib.auth.models import User
from filer.fields.image import FilerImageField

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = FilerImageField(null=True, blank=True, on_delete=models.SET_NULL)
    about = models.TextField()
    birthDate = models.DateField()
