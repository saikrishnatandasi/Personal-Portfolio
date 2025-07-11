from django.shortcuts import render
from .models import Project, Skill

# Create your views here.



def home(request):
    projects = Project.objects.all()[:3]  # Show latest 3 projects
    skills = Skill.objects.all()
    
    
    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'portfolio/home.html', context)

def projects(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/projects.html', {'projects': projects})

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')