from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
# Create your views here.


from .models import Society, Event
from .serializers import SocietySerializer, EventSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def societies(request):
    societies = Society.objects.all()
    serializer = SocietySerializer(societies, many=True)
    return Response(serializer.data)




@api_view(['GET'])
def event(request):
    event = Event.objects.all()
    serializer = EventSerializer(event, many=True)
    return Response(serializer.data)