from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project


def index(request):
    project_list = Project.objects.filter(visible = True).order_by('position')
    template = loader.get_template('index.html')
    context = {
        'project_list': project_list,
    }
    return HttpResponse(template.render(context, request))
