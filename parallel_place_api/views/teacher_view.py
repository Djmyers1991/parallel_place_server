"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Teacher
from django.contrib.auth.models import User



class Teacher_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all teachers

        Returns:
            Response -- JSON serialized list of teachers
        """

        teacher = Teacher.objects.all()
        serialized = TeacherSerializer(teacher, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single Teacher

        Returns:
            Response -- JSON serialized Teacher record
        """

        teacher = Teacher.objects.get(pk=pk)
        serialized = TeacherSerializer(teacher, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email',)

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'bio', 'favorite_book', 'representing_image', 'full_name',)