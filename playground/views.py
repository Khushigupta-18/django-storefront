from django.shortcuts import render
from .models import Trainee

def home(request):
    return render(request, 'home.html')


def trainee_list(request):
    trainees = Trainee.objects.all()
    context = {'trainees': trainees}
    return render(request, 'trainee_list.html', {'trainees': trainees})


def trainee_projects(request, trainee_id):
    trainee = Trainee.objects.get(id=trainee_id)
    projects = trainee.projects.all()
    return render(request, 'trainee_projects.html', {
        'trainee': trainee,
        'projects': projects
    })

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
