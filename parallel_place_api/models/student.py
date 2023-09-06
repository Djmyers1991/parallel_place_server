from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    perceived_iq = models.FloatField()
    overall_potential = models.FloatField()


    @property
    def full_name(self):
        return f'{self.user.first_name} {self.user.last_name}'