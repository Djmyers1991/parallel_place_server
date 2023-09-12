from django.db import models
from django.contrib.auth.models import User


class Teacher(models.Model):

    # Relationship to the built-in User model which has name and email
    user = models.OneToOneField(User, blank=True,null=True, on_delete=models.CASCADE)
    # Additional address field to capture from the client
    bio = models.CharField(max_length=155)
    favorite_book = models.CharField(max_length=60)
    representing_image = models.CharField(max_length=200)


    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'