from django.db import models

from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    team = models.CharField(max_length=50)  # Referencia por nombre
    def __str__(self):
        return self.name

class Activity(models.Model):
    user_email = models.EmailField()  # Referencia por email
    type = models.CharField(max_length=50)
    duration = models.IntegerField()
    date = models.DateField()
    def __str__(self):
        return f"{self.user_email} - {self.type}"

class Workout(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    difficulty = models.CharField(max_length=20)
    def __str__(self):
        return self.name

class Leaderboard(models.Model):
    team = models.CharField(max_length=50)  # Referencia por nombre
    points = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.team} - {self.points}"
