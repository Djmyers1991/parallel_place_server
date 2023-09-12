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
    
    def update(self, request, pk):
        update_teacher = Teacher.objects.get(pk=pk)
        update_teacher.bio = request.data["bio"]
        update_teacher.favorite_book = request.data["favorite_book"]
        update_teacher.representing_image = request.data["representing_image"]



        update_teacher.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        try:
        # Get the teacher record
            teacher = Teacher.objects.get(pk=pk)
        
        # Get the associated user
            user = teacher.user
        
        # Delete the teacher
            teacher.delete()
        
        # Delete the associated user
            user.delete()
        
            return Response(None, status=status.HTTP_204_NO_CONTENT)
        except Teacher.DoesNotExist:
            return Response({'message': 'Teacher not found.'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return Response({'message': str(ex)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email', 'first_name', 'last_name')

class TeacherSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Teacher
        fields = ('id', 'user', 'bio', 'favorite_book', 'representing_image', 'full_name',)