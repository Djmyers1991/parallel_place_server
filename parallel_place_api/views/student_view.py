"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Student
from django.contrib.auth.models import User



class Student_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        students = Student.objects.all()
        serialized = StudentSerializer(students, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        student = Student.objects.get(pk=pk)
        serialized = StudentSerializer(student, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    

    def update(self, request, pk):
        update_student = Student.objects.get(pk=pk)
        update_student.perceived_iq = request.data["perceived_iq"]
        update_student.overall_potential = request.data["overall_potential"]
        



        update_student.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Student.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','first_name', 'last_name', 'email',)

class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Student
        fields = ('id', 'user', 'perceived_iq', 'overall_potential', 'full_name')