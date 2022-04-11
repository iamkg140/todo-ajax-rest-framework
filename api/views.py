from django.shortcuts import render
from django.http import JsonResponse
from .models import Task

#import garni documentation bata yo duita line
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer

# Create your views here.

@api_view(['GET']) #eslai decorator vanxa
def apiOverview(request):
    api_urls = {
        'List' : '/task-list/',
        'Detail View' : '/task-detail/<str:pk>/',
    } 
    # return Response('API BASE POINT', safe=False)
    return Response(api_urls)

@api_view(['GET'])
def taskList(request):
    tasks = Task.objects.all().order_by('-id')
    serializer = TaskSerializer(tasks, many=True) #tyo mathi ko tasks rakhya ho do we wann seralize one obj or many? tei ho tyo
    return Response(serializer.data)

@api_view(['GET'])
def taskDetail(request,pk):
    tasks = Task.objects.get(id = pk)
    serializer = TaskSerializer(tasks, many=False) #euta obj matra teneko so many = False
    return Response(serializer.data)

@api_view(['POST'])
def taskCreate(request):
    serializer = TaskSerializer(data = request.data) # normal ma request.POST garthyo yo api vaera .data gareko 

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['POST'])
def taskUpdate(request, pk):
    task = Task.objects.get(id=pk)
    #tei data update garna instance = task garya 
    serializer = TaskSerializer(instance=task, data=request.data) # normal ma request.POST garthyo yo api vaera .data gareko 

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def taskDelete(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Item deleted successfully!')