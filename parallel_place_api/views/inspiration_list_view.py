from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Inspiration_List, Student 



class Inspiration_List_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """
        inspiration_list = Inspiration_List.objects.all()

        if "student" in request.query_params and request.query_params['student'] == "current":
            inspiration_list = Inspiration_List.filter(student__id=request.auth.user.id)
        elif "student" in request.query_params:
            pk = request.query_params['student']
            inspiration_list = inspiration_list.filter(student=pk)
        serialized = InspirationListSerializer(inspiration_list, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        inspiration_list = Inspiration_List.objects.get(pk=pk)
        serialized = InspirationListSerializer(inspiration_list, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def create(self, request):
        """Handle POST requests for service tickets

        Returns:
            Response: JSON serialized representation of newly created service ticket
        """
        new_inspiration = Inspiration_List()
        new_inspiration.student = Student.objects.get(pk=request.auth.user.id)
        new_inspiration.novel = request.data["novel"]
        new_inspiration.author = request.data["author"]
        new_inspiration.image = request.data["image"]
        new_inspiration.explanation = request.data["explanation"]
        new_inspiration.relevance_scale = request.data["relevance_scale"]
 



        new_inspiration.save()

        serialized = InspirationListSerializer(new_inspiration, many=False)

        return Response(serialized.data, status=status.HTTP_201_CREATED)

    def update(self, request, pk):
        update_inspiration = Inspiration_List.objects.get(pk=pk)
        update_inspiration.student = Student.objects.get(pk=request.auth.user.id)
        update_inspiration.novel = request.data["novel"]
        update_inspiration.author = request.data["author"]
        update_inspiration.image = request.data["image"]
        update_inspiration.explanation = request.data["explanation"]
        update_inspiration.relevance_scale = request.data["relevance_scale"]






        update_inspiration.save()
        
        return Response(None, status=status.HTTP_204_NO_CONTENT)
    
    def destroy(self, request, pk):
        post = Inspiration_List.objects.get(pk=pk)
        post.delete()
        return Response(None, status=status.HTTP_204_NO_CONTENT)

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('id', 'user', 'perceived_iq', 'overall_potential', 'full_name')

class InspirationListSerializer(serializers.ModelSerializer):
    student = StudentSerializer(many=False)
    class Meta:
        model = Inspiration_List
        fields = ('id', 'student', 'novel', 'author', 'image', 'explanation', 'relevance_scale', )