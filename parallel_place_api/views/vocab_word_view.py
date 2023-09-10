"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Vocab_Word
from django.contrib.auth.models import User
from django.db.models import Q




class Vocab_Word_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        vocab_words = Vocab_Word.objects.all()
        if "student" in request.query_params:
            vocab_words = vocab_words.filter(
            Q(creator=request.auth.user) | Q(creator__is_staff=True))
        
        
        serialized = VocabWordSerializer(vocab_words, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        vocab_word = Vocab_Word.objects.get(pk=pk)
        serialized = VocabWordSerializer(vocab_word, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
   
    def create(self, request):
        """Handle POST requests for service tickets

        Returns:
            Response: JSON serialized representation of newly created service ticket
        """
        new_word = Vocab_Word()
        new_word.creator = User.objects.get(pk=request.auth.user.id)
        new_word.definition = request.data['definition']
        new_word.name = request.data['name']




        new_word.save()

        serialized = VocabWordSerializer(new_word, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        update_word = Vocab_Word.objects.get(pk=pk)
        update_word.creator = User.objects.get(pk=request.auth.user.id)
        update_word.definition = request.data["definition"]
        update_word.name = request.data["name"]



        update_word.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        word = Vocab_Word.objects.get(pk=pk)
        word.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email', )

class VocabWordSerializer(serializers.ModelSerializer):
    creator = UserSerializer(many=False)
    class Meta:
        model = Vocab_Word
        fields = ('id', 'name', 'creator', 'definition',)