"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Assignment_Submission, Teacher, Student, Assignment
from django.contrib.auth.models import User



class Assignment_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        assignment = Assignment.objects.all()
        serialized = AssignmentSerializer(assignment, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        assignment= Assignment.objects.get(pk=pk)
        serialized = AssignmentSerializer(assignment, context={'request': request})
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
        fields = ('id', 'user', 'full_name',)
class StudentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Student
        fields = ('id', 'user', 'full_name')

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False)
    student = StudentSerializer(many=False)
    class Meta:
        model = Assignment_Submission
        fields = ('id', 'teacher', 'student', 'submission', 'teacher_feedback', 'date_reviewed', 'assignment' )


class AssignmentSerializer(serializers.ModelSerializer):
    submissions_per_assignment = AssignmentSubmissionSerializer(many=True)
    teacher = TeacherSerializer(many=False)
    class Meta:
        model = Assignment
        fields = ('id', 'teacher', 'assignment_instructions', 'title', 'submissions_per_assignment')