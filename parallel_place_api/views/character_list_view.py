from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Character_List, Assignment



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

    def create(self, request):
        """Handle POST requests for service tickets

        Returns:
            Response: JSON serialized representation of newly created service ticket
        """
        new_character = Character_List()
        new_character.assignment = Assignment.objects.get(pk=request.data['assignment'])
        new_character.name = request.data['name']
        new_character.image = request.data['image']



        new_character.save()

        serialized = CharacterListSerializer(new_character, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        character_list = Character_List.objects.get(pk=pk)
        character_list.assignment = Assignment.objects.get(pk=request.data['assignment'])
        character_list.image = request.data["image"]
        character_list.name = request.data["name"]


        character_list.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Character_List.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class CharacterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character_List
        fields = ('id', 'name', 'image', 'assignment',)