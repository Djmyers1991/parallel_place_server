"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Vocab_Word
from django.contrib.auth.models import User



class Vocab_Word_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        vocab_words = Vocab_Word.objects.all()
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