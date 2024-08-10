from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import AllowAny
from django.contrib.auth.models import User
from .models import Entry
from .serializers import UserSerializer, EntrySerializer

# Create your views here.
class CreateEntry(generics.ListCreateAPIView):
  serializer_class = EntrySerializer
  permission_classes = [AllowAny]

  def get_queryset(self):
    user = self.request.user
    return Entry.objects.filter(author=user)
  
  def perform_create(self, serializer):
    if serializer.is_valid():
      serializer.save(author=self.request.user)
    else:
      print(serializer.errors)

class DeleteEntry(generics.DestroyAPIView):
  serializer_class = EntrySerializer
  permission_classes = [AllowAny]

  def get_queryset(self):
    user = self.request.user
    return Entry.objects.filter(author=user)
  
class CreateUser(generics.CreateAPIView):
  queryset = User.objects.all()
  serializer_class = UserSerializer
  permission_classes = [AllowAny]