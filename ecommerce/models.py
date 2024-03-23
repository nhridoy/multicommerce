from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group, Permission


class DailyData(models.Model):
    date = models.DateField()
    revenue = models.DecimalField(max_digits=10, decimal_places=2)
