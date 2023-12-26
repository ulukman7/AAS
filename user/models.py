from django.db import models
from django.contrib.auth.models import AbstractUser
from .choices import TypeOfAward


class Award(models.Model):
    name = models.CharField(max_length=255)
    type_award = models.CharField(verbose_name='тип награды', max_length=100, choices=TypeOfAward.choices, null=True, blank=True)


class User(AbstractUser):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    award = models.ForeignKey(Award, on_delete=models.CASCADE)



