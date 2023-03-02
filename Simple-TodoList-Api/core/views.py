from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from api.serializers import TaskSerializer
# Create your views here.

@api_view(['GET'])
def Homeview(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def DetailView(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def CreateView(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def UpdateView(request, pk):
    tasks = Task.objects.get(pk=pk)
    serializer = TaskSerializer(data=request.data, instance=tasks)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteView(request, pk):
    tasks = Task.objects.get(pk=pk)
    tasks.delete()
    return Response('Deleted Successfully')