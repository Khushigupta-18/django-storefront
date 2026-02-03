# Register your models here.
from django.contrib import admin
from .models import Trainee, Project, Status

admin.site.register(Trainee)
admin.site.register(Project)
admin.site.register(Status)
