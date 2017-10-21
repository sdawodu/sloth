from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from tracker.models import (
    Exercise,
    Plan,
    Phase,
    Period,
    Workout,
    Set,
)

from tracker.serializers import (
    ExerciseSerializer,
    PlanSerializer,
    PhaseSerializer,
    PeriodSerializer,
    WorkoutSerializer,
    SetSerializer,
)
from rest_framework import generics


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


class ExerciseList(generics.ListCreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer


class PlanList(generics.ListCreateAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Plan.objects.all()
    serializer_class = PlanSerializer


class PhaseList(generics.ListCreateAPIView):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer


class PhaseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Phase.objects.all()
    serializer_class = PhaseSerializer


class PeriodList(generics.ListCreateAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class PeriodDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Period.objects.all()
    serializer_class = PeriodSerializer


class WorkoutList(generics.ListCreateAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class WorkoutDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Workout.objects.all()
    serializer_class = WorkoutSerializer


class SetList(generics.ListCreateAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer


class SetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Set.objects.all()
    serializer_class = SetSerializer
