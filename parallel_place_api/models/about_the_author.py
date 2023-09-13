from django.db import models


class About_The_Author(models.Model):
    teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE, null=True)
    introduction = models.CharField(max_length=7000000)
