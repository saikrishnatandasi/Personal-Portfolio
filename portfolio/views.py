from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings


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

def contact_view(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject', 'New Contact Form Submission')
        message = request.POST.get('message')

        full_message = f"From: {name} <{email}>\n\n{message}"

        send_mail(
            subject,
            full_message,
            settings.EMAIL_HOST_USER,
            ['saikrishnatandasi2001@gmail.com'],  # Where you want to receive the message
            fail_silently=False,
        )

        return render(request, 'portfolio/success.html')

    
    return render(request, 'portfolio/home.html')
