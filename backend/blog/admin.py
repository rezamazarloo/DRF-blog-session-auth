from django.contrib import admin

from .models import Badge, Post, ImageGallery

# Register your models here.
class ImageGalleryInlineAdmin(admin.StackedInline):
    model = ImageGallery

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model: Post
    inlines = [ImageGalleryInlineAdmin]

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    model: Badge
