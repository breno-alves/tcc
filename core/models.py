from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    gender_choices = (('Male', 'Male'), ('Female', 'Female'))

    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=11, choices=gender_choices)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def get_permission(self):
        pass


class Medic(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    crm = models.CharField(max_length=256)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Pharmaceutical(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
