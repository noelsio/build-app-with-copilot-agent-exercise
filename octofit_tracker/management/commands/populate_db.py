from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrar datos existentes
        User.objects.all().delete()
        Team.objects.all().delete()
        Activity.objects.all().delete()
        Leaderboard.objects.all().delete()
        Workout.objects.all().delete()

        # Crear equipos
        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        # Crear usuarios
        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team=marvel.name)
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team=marvel.name)
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team=dc.name)
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team=dc.name)

        # Crear actividades
        Activity.objects.create(user=tony, type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user=steve, type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user=bruce, type='Swimming', duration=60, date=timezone.now())
        Activity.objects.create(user=clark, type='Yoga', duration=20, date=timezone.now())

        # Crear workouts
        Workout.objects.create(name='HIIT', description='High Intensity Interval Training', difficulty='Hard')
        Workout.objects.create(name='Cardio', description='Cardio session', difficulty='Medium')
        Workout.objects.create(name='Strength', description='Strength training', difficulty='Hard')

        # Crear leaderboard
        Leaderboard.objects.create(team=marvel, points=100)
        Leaderboard.objects.create(team=dc, points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
