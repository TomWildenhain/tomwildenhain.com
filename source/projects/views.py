from django.shortcuts import render
from django.http import HttpResponse, Http404
from projects.models import Project

# Create your views here.

def projects(request):
    projects = Project.objects.order_by('index')
    context = {'projects': projects}
    return render(request, 'projects/projects.html', context)