from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import datetime

# Create your models here.

class ForumGroups(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField()
    image_url = models.TextField()
    delete_time = models.DateField(default=timezone.now)
   

    def __str__(self):
        return f"{self.name} {self.delete_time}"

class ForumAddLog(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    group_name = models.ForeignKey(ForumGroups,on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    track_unit = models.IntegerField()
    

    def __str__(self):
        return f"{self.user.username} | {self.group_name.name}  | {self.date} | {self.track_unit}"
    
class Previous_Group(models.Model):
    name = models.CharField(max_length=70)
    desc = models.TextField()
    image_url = models.TextField()
    winner_user = models.CharField(max_length=70,null=True)

    def __str__(self):
        return f"{self.name} | Winner:{self.winner_user}"
    