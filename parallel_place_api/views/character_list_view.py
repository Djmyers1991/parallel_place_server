from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Character_List



class Character_List_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        character_List = Character_List.objects.all()
        serialized = CharacterListSerializer(character_List, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        character_list = Character_List.objects.get(pk=pk)
        serialized = CharacterListSerializer(character_list, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)


class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_List
        fields = ('id', 'name', 'image', 'assignment_id',)