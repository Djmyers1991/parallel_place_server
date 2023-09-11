"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from django.contrib.auth.models import User

class UserView(ViewSet):
    """Handles requests for shutterbug users"""
    def list(self, request):
        """Handle GET requests to shutterbug users resource"""
       
        users = User.objects.all()
            
        if "current" in request.query_params:
            users = users.filter(user=request.auth.user)
            
        serializer = UserSerializer(users, many=True, context={'request': request})
        return Response(serializer.data)
    
    def retrieve(self, request, pk=None):
        """Handle GET requests for single Teacher

        Returns:
            Response -- JSON serialized Teacher record
        """

        user = User.objects.get(pk=pk)
        serialized = UserSerializer(user, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def update(self, request, pk):
        update_user = User.objects.get(pk=pk)
        update_user.first_name = request.data["first_name"]
        update_user.last_name = request.data["last_name"]
        update_user.email = request.data["email"]

        update_user.save()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


            # Fields to exclude from updating

        



class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'first_name', 'last_name', 'username','email',)