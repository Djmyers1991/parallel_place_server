from django.db import models


class Assignment(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True, related_name='assignments_by_teacher')
    title = models.CharField(max_length=70)
    assignment_instructions = models.CharField(max_length=1000)