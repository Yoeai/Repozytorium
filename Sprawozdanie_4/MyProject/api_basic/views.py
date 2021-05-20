from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Game
from .serializers import GameSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins

# Create your views here.

class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin,mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = GameSerializer
    queryset = Game.objects.all()

    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)
        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)



class GameAPIView(APIView):
    def get(self, request):
        Games = Game.objects.all()
        serializer = GameSerializer(Games, many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','POST'])
def Game_list(request):
    if request.method == 'GET':
        Games = Game.objects.all()
        serializer = GameSerializer(Games, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = GameSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def Game_detail(request, pk):
    try:
        Game = Game.objects.get(pk=pk)

    except Game.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = GameSerializer(Game)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GameDetails(APIView):
    def get_object(self, id):
        try:
            return Game.objects.get(id=id)

        except Game.DoesNotExist:
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    def get(self, request, id):
        Game = self.get_object(id)
        serializer = GameSerializer(Game)
        return Response(serializer.data)

    def put(self, request, id):
        Game = self.get_object(id)
        serializer = GameSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, id):
        Game = self.get_object(id)
        Game.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)