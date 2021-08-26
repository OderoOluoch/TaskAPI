from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import Task


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'EndPoint':'api/v1/tasks/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of tasks'
        },
         {
            'EndPoint':'api/v1/tasks/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single task object based on id'
        },
         {
            'EndPoint':'api/v1/tasks/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates a new task object with data send using POST request'
        },
         {
            'EndPoint':'api/v1/task/id/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Updates Existing task Object with new data coming in from Post request'
        },
         {
            'EndPoint':'api/v1/task/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an exiting task object based on provided id'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getTasks(request):
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getTask(request, pk):
    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    data = request.data

    task = Task.objects.create(
        title=data['title'],
        detail=data['detail']
    )
    serializer = TaskSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data

    task = Task.objects.get(id=pk)
    serializer = TaskSerializer(task,data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Task.objects.get(id=pk)
    task.delete()
    return Response('Task was deleted!')