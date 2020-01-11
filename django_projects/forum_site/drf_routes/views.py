from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from django.contrib.auth.models import User


class GetUsersCount(generics.GenericAPIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        users = User.objects.count()
        return Response(data={'users count': users})
