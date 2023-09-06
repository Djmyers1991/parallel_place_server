"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import Discussion_Comment
from django.contrib.auth.models import User



class Discussion_Comment_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        discussion_comments = Discussion_Comment.objects.all()
        serialized = DiscussionCommentSerializer(discussion_comments, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        discussion_comment = Discussion_Comment.objects.get(pk=pk)
        serialized = DiscussionCommentSerializer(discussion_comment, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for Teachers"""
    class Meta:
        model = User
        fields = ('id', 'is_staff', 'username','email', 'first_name', 'last_name')

class DiscussionCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)
    class Meta:
        model = Discussion_Comment
        fields = ('id', 'user', 'response', 'discussion_topic', )