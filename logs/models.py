from django.db import models
from account.models import User


# Create your models here.


class Log(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    date = models.DateTimeField()
    log = models.CharField(max_length=1000)