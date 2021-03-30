from django.db import models
import datetime
from django.utils import timezone


class Message(models.Model):
    teacher_name = models.CharField(max_length=20)
    time13_1 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time13_2 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time14_1 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time14_2 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time17_1 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time17_2 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time18_1 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time18_2 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time20_1 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    time20_2 = models.CharField(max_length=20,default=" ",null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

    def __str__(self):
        return u"{0}:{1}... ".format(self.id, self.teacher_name[:10])