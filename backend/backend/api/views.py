from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Entry
from .serializer import EntrySerializer

# Create your views here.
@api_view(['POST'])
def create_entry(request):
  serializer = EntrySerializer(data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_201_CREATED)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def list_entries(request):
  entries = Entry.objects.all()
  serializer = EntrySerializer(entries, many=True)
  return Response(serializer.data)

@api_view(['GET'])
def get_entry(request, pk):
  try:
    entry = Entry.objects.get(pk=pk)
  except Entry.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  serializer = EntrySerializer(entry)
  return Response(serializer.data)

@api_view(['PUT'])
def update_entry(request, pk):
  try:
    entry = Entry.objects.get(pk=pk)
  except Entry.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  serializer = EntrySerializer(entry, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def delete_entry(request, pk):
  try:
    entry = Entry.objects.get(pk=pk)
  except Entry.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)
  
  entry.delete()
  return Response(status=status.HTTP_204_NO_CONTENT)