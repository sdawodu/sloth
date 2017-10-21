from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Exercise(models.Model):
    name = models.CharField(max_length=256)
    notes = models.TextField(blank=True, null=True)
    video_link = models.URLField(blank=True, null=True)

    # Assume every exercise is done for reps unless otherwise stated
    is_timed = models.BooleanField()

    def __str__(self):
        return self.name


class Person(models.Model):
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    role = models.CharField(
        choices=[
            ('trainer', 'trainer'),
            ('trainee', 'trainee')
        ],
        max_length=7
    )
    trainer = models.ForeignKey('Person', blank=True, null=True)

    def __str__(self):
        return str(self.user)


class Plan(models.Model):
    trainee = models.ForeignKey(Person, blank=True, null=True)
    goals = models.TextField()
    is_active = models.BooleanField()
    status = models.CharField(
        choices=[
            ('development', 'development'),
            ('active', 'active'),
            ('complete', 'complete'),
            ('cancelled', 'cancelled'),
        ],
        max_length=12
    )

    def __str__(self):
        return "{}:{}".format(self.trainee, self.status)


class Phase(models.Model):
    name = models.CharField(max_length=64)
    goals = models.TextField()

    # Default to 6 periods in a phase.
    periods = models.IntegerField(default=6)

    plan = models.ForeignKey(Plan)
    # To Do:
    # - Add some methods to assess success of phase

    def __str__(self):
        return self.name


class Period(models.Model):
    name = models.CharField(max_length=64)
    notes = models.TextField()

    # Default to programming by week
    length = models.IntegerField(default=7)
    phase = models.ForeignKey(Phase)

    def __str__(self):
        return self.name


class Workout(models.Model):
    name = models.CharField(max_length=256)
    notes = models.TextField()
    period = models.ForeignKey(Period)
    sets = models.ManyToManyField('Set')

    def __str__(self):
        return self.name


class Set(models.Model):
    exercise = models.ForeignKey(Exercise)
    reps = models.IntegerField(blank=True, null=True)
    time = models.IntegerField(blank=True, null=True)
    is_amrap = models.BooleanField()
    is_complete = models.BooleanField()

    reps_done = models.IntegerField(blank=True, null=True)
    time_done = models.TimeField(blank=True, null=True)
    # workout = models.ForeignKey(Workout)

    def __str__(self):
        return "{0}:{1}".format(self.exercise, self.reps or self.time)
