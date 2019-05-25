from django.db import models
from django.contrib.auth.models import User
from hashlib import md5


# Create your models here.
class Flag(models.Model):
    name = models.CharField(max_length=100, unique=True)
    code = models.CharField(max_length=250, unique=True)
    points = models.IntegerField()

    def __str__(self):
        return self.name

    def make_code_md5(self):
        return md5(self.code.encode()).hexdigest()

    def save(self, *args, **kwargs):
        self.code = self.make_code_md5()
        super().save(*args, **kwargs)


class Capture(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    flag = models.ForeignKey(Flag, on_delete=models.CASCADE)
    time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{} captured by {}'.format(self.flag, self.user)


class Team(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class TeamMember(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return '{} of {}'.format(self.user, self.team)


class Setting(models.Model):
    name = models.CharField(max_length=30, unique=True)
    value = models.CharField(max_length=30, unique=True)
