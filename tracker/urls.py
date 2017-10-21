from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^exercises/$', views.ExerciseList.as_view()),
    url(r'^exercise/(?P<pk>[0-9]+)/$', views.ExerciseDetail.as_view()),
    url(r'^plans/$', views.PlanList.as_view()),
    url(r'^plan/(?P<pk>[0-9]+)/$', views.PlanDetail.as_view()),
    url(r'^phases/$', views.PhaseList.as_view()),
    url(r'^phase/(?P<pk>[0-9]+)/$', views.PhaseDetail.as_view()),
    url(r'^periods/$', views.PeriodList.as_view()),
    url(r'^period/(?P<pk>[0-9]+)/$', views.PeriodDetail.as_view()),
    url(r'^workkouts/$', views.WorkoutList.as_view()),
    url(r'^workkout/(?P<pk>[0-9]+)/$', views.WorkoutDetail.as_view()),
    url(r'^sets/$', views.SetList.as_view()),
    url(r'^set/(?P<pk>[0-9]+)/$', views.SetDetail.as_view()),
]
