from django.db import models
from django.contrib.auth.models import User


class Discussion_Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="user_comments")
    response = models.CharField(max_length=10000)
    discussion_topic = models.ForeignKey("Discussion_Topic", on_delete=models.DO_NOTHING, related_name='discussion_comments')

