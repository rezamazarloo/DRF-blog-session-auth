from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import AuthorUserMixin
from .serializers import ProfileSerializer
from .models import Profile


class AuthorProfileAPI(AuthorUserMixin, RetrieveAPIView):
    serializer_class = ProfileSerializer

    def get_object(self):
        return Profile.objects.get(user=self.request.user)