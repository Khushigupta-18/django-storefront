from django.conf import settings
from django.urls import path
from . import views

app_name = 'playground'

urlpatterns = [
    path('trainees/', views.trainee_list, name='trainee_list'),
    path('trainees/<int:trainee_id>/', views.trainee_projects, name='trainee_projects'),
]


