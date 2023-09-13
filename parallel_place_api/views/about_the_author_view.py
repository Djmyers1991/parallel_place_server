"""View module for handling requests for customer data"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from parallel_place_api.models import About_The_Author
from django.contrib.auth.models import User



class About_The_Author_View(ViewSet):

    def list(self, request):
        """Handle GET requests to get all students

        Returns:
            Response -- JSON serialized list of students
        """

        about_the_authors = About_The_Author.objects.all()
        serialized = AboutTheAuthorSerializer(about_the_authors, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None):
        """Handle GET requests for single student

        Returns:
            Response -- JSON serialized student record
        """

        about_the_author = About_The_Author.objects.get(pk=pk)
        serialized = AboutTheAuthorSerializer(about_the_author, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)
   
#     def create(self, request):
#         """Handle POST requests for service tickets

#         Returns:
#             Response: JSON serialized representation of newly created service ticket
#         """
#         new_topic = Discussion_Topic()
#         new_topic.teacher = Teacher.objects.get(pk=request.data['teacher'])
#         new_topic.writing_prompt = request.data['writing_prompt']



#         new_topic.save()

#         serialized = DiscussionTopicSerializer(new_topic, many=False)

#         return Response(serialized.data, status=status.HTTP_201_CREATED)

#     def update(self, request, pk):
#         update_topic = Discussion_Topic.objects.get(pk=pk)
#         update_topic.teacher = Teacher.objects.get(pk=request.data['teacher'])
#         update_topic.writing_prompt = request.data["writing_prompt"]


#         update_topic.save()
        
#         return Response(None, status=status.HTTP_204_NO_CONTENT)
    
#     def destroy(self, request, pk):
#         post = Discussion_Topic.objects.get(pk=pk)
#         post.delete()
#         return Response(None, status=status.HTTP_204_NO_CONTENT)

# class UserSerializer(serializers.ModelSerializer):
#     """JSON serializer for Teachers"""
#     class Meta:
#         model = User
#         fields = ('id', 'is_staff', 'email', 'first_name', 'last_name')

# class TeacherSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)
#     class Meta:
#         model = Teacher
#         fields = ('id', 'user', 'full_name',)

# class DiscussionCommentSerializer(serializers.ModelSerializer):
#     user = UserSerializer(many=False)
#     class Meta:
#         model = Discussion_Comment
#         fields = ('id', 'user', 'response', 'discussion_topic', )

class AboutTheAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = About_The_Author
        fields = ('id', 'teacher', 'introduction',)