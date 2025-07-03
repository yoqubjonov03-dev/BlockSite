from django.shortcuts import render
from rest_framework import viewsets
from .serializers import UsernameSerializer
from .models import User
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UsernameSerializer
    # permission_classes = [IsAuthenticated]
