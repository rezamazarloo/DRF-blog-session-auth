from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, User
from django.contrib.auth.mixins import LoginRequiredMixin 

# Create your views here.
class AuthorProfileAPI(LoginRequiredMixin, APIView):
    def put(self, request, *args, **kwargs):
        print(request.user.groups.all())
        return Response(self.request.user.groups.filter(name="author"), status=status.HTTP_200_OK)