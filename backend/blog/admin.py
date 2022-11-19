from django.contrib import admin

from .models import Badge, Post, ImageGallery

# Register your models here.
class ImageGalleryInlineAdmin(admin.StackedInline):
    model = ImageGallery

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    inlines = [ImageGalleryInlineAdmin]
    list_display = ("__str__", "isPublished", "createdAt", "publishedAt")

@admin.register(Badge)
class BadgeAdmin(admin.ModelAdmin):
    model = Badge
