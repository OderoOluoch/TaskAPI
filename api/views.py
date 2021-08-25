from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import NoteSerializer
from .models import Note


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'EndPoint':'/notes/',
            'method':'GET',
            'body':None,
            'description':'Returns an array of notes'
        },
         {
            'EndPoint':'/notes/id',
            'method':'GET',
            'body':None,
            'description':'Returns a single notes object based on id'
        },
         {
            'EndPoint':'/notes/create',
            'method':'POST',
            'body':{'body':""},
            'description':'Creates a new notes object with data send using POST request'
        },
         {
            'EndPoint':'/notes/id/update',
            'method':'PUT',
            'body':{'body':""},
            'description':'Updates Existing Notes Object with new data coming in from Post request'
        },
         {
            'EndPoint':'/notes/id/delete',
            'method':'DELETE',
            'body':None,
            'description':'Deletes an exiting notes object based on provided id'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getNotes(request):
    notes = Note.objects.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def getNote(request, pk):
    note = Note.objects.get(id=pk)
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createNote(request):
    data = request.data

    note = Note.objects.create(
        body=data['body']
    )
    serializer = NoteSerializer(note, many=False)
    return Response(serializer.data)