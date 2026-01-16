from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from django.utils import timezone

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Borrado seguro por colección
        try:
            Activity.objects.all().delete()
        except Exception:
            pass
        try:
            Leaderboard.objects.all().delete()
        except Exception:
            pass
        try:
            User.objects.all().delete()
        except Exception:
            pass
        try:
            Workout.objects.all().delete()
        except Exception:
            pass
        try:
            Team.objects.all().delete()
        except Exception:
            pass


        marvel = Team.objects.create(name='Marvel', description='Marvel superheroes')
        dc = Team.objects.create(name='DC', description='DC superheroes')

        tony = User.objects.create(name='Tony Stark', email='tony@marvel.com', team='Marvel')
        steve = User.objects.create(name='Steve Rogers', email='steve@marvel.com', team='Marvel')
        bruce = User.objects.create(name='Bruce Wayne', email='bruce@dc.com', team='DC')
        clark = User.objects.create(name='Clark Kent', email='clark@dc.com', team='DC')

        Activity.objects.create(user_email='tony@marvel.com', type='Running', duration=30, date=timezone.now())
        Activity.objects.create(user_email='steve@marvel.com', type='Cycling', duration=45, date=timezone.now())
        Activity.objects.create(user_email='bruce@dc.com', type='Swimming', duration=60, date=timezone.now())
        Activity.objects.create(user_email='clark@dc.com', type='Yoga', duration=20, date=timezone.now())

        Workout.objects.create(name='HIIT', description='High Intensity Interval Training', difficulty='Hard')
        Workout.objects.create(name='Cardio', description='Cardio session', difficulty='Medium')
        Workout.objects.create(name='Strength', description='Strength training', difficulty='Hard')

        Leaderboard.objects.create(team='Marvel', points=100)
        Leaderboard.objects.create(team='DC', points=80)

        self.stdout.write(self.style.SUCCESS('octofit_db database populated with test data'))
