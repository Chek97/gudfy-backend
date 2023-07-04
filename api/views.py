from django.shortcuts import render
from rest_framework.views import APIView
from .models import Task
from .serializers import TaskSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TaskView(APIView):
    # Get all the tasks
    def get(self, request, format=None, *args, **kwargs):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)

        return Response(serializer.data)
    
    def post(self, request, format=None):
        serializer = TaskSerializer(data=request.data)
        if (serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk, format=None, *args, **kwargs):
        task = Task.objects.get(pk=pk)
        serializer = TaskSerializer(task, data = request.data, partial = True)
        if (serializer.is_valid()):
            serializer.save()
            return Response({"ok": True, "data": serializer.data})
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)