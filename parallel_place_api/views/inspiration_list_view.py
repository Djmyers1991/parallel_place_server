from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Inspiration_List



class Inspiration_List_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        inspiration_list = Inspiration_List.objects.all()
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


class InspirationListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inspiration_List
        fields = ('id', 'student', 'novel', 'author', 'image', 'explanation', 'relevance_scale', 'assignment')