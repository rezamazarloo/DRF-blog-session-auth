from django.contrib import admin
from django.urls import path, include
from .apis import AuthorProfileAPI


urlpatterns = [
    path("author/", AuthorProfileAPI.as_view(), name="profile"),
]