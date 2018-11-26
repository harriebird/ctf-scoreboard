from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Flag(models.Model):
    code = models.CharField(max_length=250)
    points = models.IntegerField()

    def __str__(self):
        return self.code

class Capture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    time = models.TimeField(auto_now=True)

    def __str__(self):
        return '{} captured by {}'.format(self.flag.code, self.user)
