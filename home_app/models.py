from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from datetime import date


# Create your models here.

#SQlite db used which is django builtin database
# This will save user,first and last name to database
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Confirm_email = models.EmailField(default='null')
    coins = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user} {self.coins}"

# Habit saved to database
class Habit(models.Model):
    title = models.CharField(max_length=100,null=False)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)
    goal = models.IntegerField(default=0,null=False)
    goal_unit = models.CharField(max_length=70,null=False)

    
    def __str__(self):
        return f"Title: {self.title} | author: {self.author} | Goal: {self.goal} | Unit: {self.goal_unit}"

# Habit log saved to database
class HabitLog(models.Model):
    habit = models.ForeignKey(
        Habit, on_delete=models.CASCADE, blank=True, null=True, related_name='habit_track'
    )
    date = models.DateField(default=date.today())
    track_unit = models.IntegerField(default=0)


    def __str__(self):
        return f"Name:{self.habit} | Date: {self.date} | Amount: {self.track_unit}"
    
