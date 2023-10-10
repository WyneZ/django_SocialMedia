from rest_framework.decorators import api_view
from rest_framework.response import Response
from base.models import Room
from .serializers import RoomSerializer


# to show all routes in our api
@api_view(['GET'])
def getRoute(request):
    routes = [
        'GET /api',
        'GET /api/rooms',
        'GET /api/rooms/:id'
    ]

    # return JsonResponse(routes, safe=False)  # safeဆိုတာ JsonResponseထဲမှာ py dictအပြင် အခြား(like list, etc)တွေပါသုံးရအောင် falseထားတာ
    return Response(routes)


@api_view(['GET'])
def getRooms(request):
    rooms = Room.objects.all()
    serializer = RoomSerializer(rooms, many=True)  # many means multiple objects to serialize | not one serializing
    return Response(serializer.data)


@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=pk)
    serializer = RoomSerializer(room, many=False)  # many means multiple objects to serialize | not one serializing
    return Response(serializer.data)
