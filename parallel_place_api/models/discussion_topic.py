from django.db import models


class Discussion_Topic(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.DO_NOTHING, related_name='topics_by_teacher')
    writing_prompt = models.CharField(max_length=1170)

    