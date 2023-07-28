from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.core.exceptions import ObjectDoesNotExist

from .models import ToDoItem, Profile
from .serializers import ToDoItemSerializer

class ToDoList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


    def get(self, request):
        profile = request.user.profile

        qs = ToDoItem.objects.filter(profile = profile)
        serializer = ToDoItemSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ToDoItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.context.update({'profile':request.user.profile})
        serializer.save()
        return Response('ok',status=status.HTTP_201_CREATED)


class ToDoDetail(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        try:
            item = ToDoItem.objects.get(pk=pk, profile = request.user.profile)
            serializer = ToDoItemSerializer(item)
            return Response(serializer.data)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        

    def patch(self, request, pk):
        try:
            item = ToDoItem.objects.get(pk=pk, profile = request.user.profile)
            serializer = ToDoItemSerializer(item, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data)
        
        except ObjectDoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)