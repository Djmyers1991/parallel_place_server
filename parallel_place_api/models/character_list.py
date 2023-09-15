from django.db import models


class Character_List(models.Model):
    assignment = models.ForeignKey("Assignment", on_delete=models.DO_NOTHING, related_name='characters')
    name = models.CharField(max_length=70)
