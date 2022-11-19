from django.db import models


class CreatedUpdatedFields(models.Model):
    createdAt = models.DateTimeField(auto_now_add=True, verbose_name="Created at")
    updatedAt = models.DateTimeField(auto_now=True, verbose_name="Updated at")

    class Meta:
        abstract = True
