from django.shortcuts import render
from django.http import HttpResponse, Http404
from resume.models import *

# Create your views here.

def resume(request):
    education = Education.objects.order_by('index')
    experience = Experience.objects.order_by('index')
    projects = Project.objects.order_by('index')
    skills = Skill.objects.order_by('-confidence')
    context = {
        'education': education,
        'experience': experience,
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'resume/resume.html', context)