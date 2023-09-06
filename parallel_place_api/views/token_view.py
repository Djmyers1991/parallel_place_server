from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User



class Token_View(ViewSet):

    def retrieve(self, request, pk):
        token = Token.objects.get(pk=pk)
        serializer = TokenSerializer(token)
        return Response(serializer.data)

    def list(self, request):
        tokens = Token.objects.all()
        serializer = TokenSerializer(tokens, many=True)
        return Response(serializer.data)
    
class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email',)
        
class TokenSerializer(serializers.ModelSerializer):
    user= UserSerializer(many=False)
    class Meta:
        model = Token
        fields = ('user', 'created')
