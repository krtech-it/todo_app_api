from django.shortcuts import render

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializes import TaskSerializer
from .models import Task


@api_view(['GET'])
def apiOverview(request):
    api_list = {
        'List': '/task-list/',
        'Detail': 'task-detail/<int:pk>/',
        'Create': 'task-create/',
        'Update': 'task-update/<int:pk>/',
        'Delete': 'task-delete/<int:pk>/'
    }
    return Response(api_list)


@api_view(["GET"])
def taskList(request):
    tasks = Task.objects.all().order_by('id')
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def taskDetail(request, pk):
    tasks = Task.objects.get(id=pk)
    serializer = TaskSerializer(tasks, many=False)
    return Response(serializer.data)


@api_view(["POST"])
def taskCreate(request):
    serializer = TaskSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["POST"])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(instance=task, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(["DELETE"])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item succsesfully delete!')
