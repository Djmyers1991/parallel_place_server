"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Assignment_Submission, Teacher, Student, Assignment
from django.contrib.auth.models import User
from django.db.models import Q




class Assignment_Submission_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        assignment_submissions = Assignment_Submission.objects.order_by('-date_reviewed')
        if "student" in request.query_params:
            assignment_submissions = assignment_submissions.filter(student__id=request.auth.user.id)
        elif "completedstudent" in request.query_params:
            assignment_submissions = assignment_submissions.filter(Q(date_reviewed__isnull=False) & Q(student__id=request.auth.user.id))
        elif "incomplete" in request.query_params:
            assignment_submissions = assignment_submissions.filter(Q(date_reviewed__isnull=True) & Q(teacher = None ))
        elif "currentungraded" in request.query_params:
            assignment_submissions = assignment_submissions.filter(Q(date_reviewed__isnull=True) & Q(teacher__id = request.auth.user.id ))
        elif "graded" in request.query_params:
            assignment_submissions = assignment_submissions.filter(Q(date_reviewed__isnull=False) & Q(teacher__id = request.auth.user.id ))
        elif "unreviewedstudent" in request.query_params:
            assignment_submissions = assignment_submissions.filter(Q(date_reviewed__isnull=True) & Q(student__id=request.auth.user.id))

            
        serialized = AssignmentSubmissionSerializer(assignment_submissions, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        assignment_submission = Assignment_Submission.objects.get(pk=pk)
        serialized = AssignmentSubmissionSerializer(assignment_submission, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        """Handle POST requests for service tickets

        Returns:
            Response: JSON serialized representation of newly created service ticket
        """
        new_submission = Assignment_Submission()
        try:
            teacher_pk = request.data.get('teacher')  # Assuming request.data is a dictionary
            if teacher_pk is not None:  # Check if the 'teacher' key is present in the data
                new_submission.teacher = Teacher.objects.get(pk=teacher_pk)
            else:
                new_submission.teacher = None  # Assign None if 'teacher' is not provided
        except Teacher.DoesNotExist:
            new_submission.teacher = None  # Handle the case where the teacher doesn't exist
        new_submission.student = Student.objects.get(pk=request.data['student'])
        new_submission.submission = request.data['submission']
        new_submission.teacher_feedback = request.data['teacher_feedback']
        new_submission.date_reviewed = request.data['date_reviewed']
        new_submission.assignment = Assignment.objects.get(pk=request.data["assignment"])




        new_submission.save()

        serialized = AssignmentSubmissionSerializer(new_submission, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        """handles PUT requests for updating a Comment"""
        assignment_submission = Assignment_Submission.objects.get(pk=pk)
        try:
            teacher_pk = request.data.get('teacher')  # Assuming request.data is a dictionary
            if teacher_pk is not None:  # Check if the 'teacher' key is present in the data
                assignment_submission.teacher = Teacher.objects.get(pk=teacher_pk)
            else:
                assignment_submission.teacher = None  # Assign None if 'teacher' is not provided
        except Teacher.DoesNotExist:
            assignment_submission.teacher = None  # Handle the case where the teacher doesn't exist
        assignment_submission.student = Student.objects.get(pk=request.data['student'])
        assignment_submission.assignment = Assignment.objects.get(pk=request.data['assignment'])
        assignment_submission.submission = request.data["submission"]
        assignment_submission.teacher_feedback = request.data["teacher_feedback"]
        assignment_submission.date_reviewed = request.data["date_reviewed"]


        assignment_submission.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Assignment_Submission.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)


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

class AssignmentSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False)
    class Meta:
        model = Assignment
        fields = ('id', 'teacher', 'assignment_instructions', 'title', 'submissions_per_assignment')

class AssignmentSubmissionSerializer(serializers.ModelSerializer):
    teacher = TeacherSerializer(many=False)
    student = StudentSerializer(many=False)
    assignment = AssignmentSerializer(many=False)
    class Meta:
        model = Assignment_Submission
        fields = ('id', 'teacher', 'student', 'submission', 'teacher_feedback', 'date_reviewed', 'assignment' )