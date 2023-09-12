from django.db import models
from django.contrib.auth.models import User


class Vocab_Word(models.Model):
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='vocab_words_by_user')
    name = models.CharField(max_length=70)
    definition = models.CharField(max_length=200)


