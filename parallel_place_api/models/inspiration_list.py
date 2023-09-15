from django.db import models


class Inspiration_List(models.Model):
    student = models.ForeignKey("Student", on_delete=models.DO_NOTHING, related_name='student_inspirational_books')
    novel = models.CharField(max_length=70)
    author = models.CharField(max_length=50)
    image = models.CharField(max_length=5000)
    explanation = models.CharField(max_length=5000)
    relevance_scale = models.FloatField()
    


