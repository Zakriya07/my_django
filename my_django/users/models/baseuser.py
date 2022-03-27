from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import ArrayField
from base.choices import ROLE_CHOICE,GENDER_CHOICE

class User(AbstractUser):
    gender=models.PositiveSmallIntegerField(choices=GENDER_CHOICE,default=1)
    role=models.PositiveSmallIntegerField(choices=ROLE_CHOICE,default=2)

    def __str__(self) -> str:
        return self.username

