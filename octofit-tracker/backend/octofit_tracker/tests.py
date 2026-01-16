from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class ModelTestCase(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel superheroes')
        self.user = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=self.team)
        self.workout = Workout.objects.create(name='HIIT', description='High Intensity', difficulty='Hard')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2023-01-01')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user(self):
        self.assertEqual(self.user.name, 'Tony Stark')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_team(self):
        self.assertEqual(self.team.name, 'Marvel')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')

    def test_workout(self):
        self.assertEqual(self.workout.difficulty, 'Hard')

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
