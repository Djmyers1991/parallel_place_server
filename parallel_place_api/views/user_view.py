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
        try:
            users = User.objects.all()
            
            if "current" in request.query_params:
                users = users.filter(user=request.auth.user)
            
            serializer = UserSerializer(users, many=True, context={'request': request})
            return Response(serializer.data)


        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email',)