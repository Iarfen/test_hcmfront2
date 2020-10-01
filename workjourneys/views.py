# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader

from .models import Workjourneys


def index(request):
    workjourneys_list = Workjourneys.objects.order_by('id')[:5]
    template = loader.get_template('workjourneys/index.html')
    context = {
        'workjourneys_list': workjourneys_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, workjourney_id):
    workjourney = Workjourneys.objects.get(pk=workjourney_id)
    template = loader.get_template('workjourneys/detail.html')
    context = {
        'workjourney': workjourney,
    }
    return HttpResponse(template.render(context, request))

def create(request):
    template = loader.get_template('workjourneys/create.html')
    return HttpResponse(template.render({}, request))

def create_send(request):
    w = Workjourneys(name=request.POST['name'],code=request.POST['code'],schedule=request.POST['schedule'])
    w.save()
    return HttpResponseRedirect('/workjourneys/' + str(w.id))

def delete(request, workjourney_id):
    workjourney = Workjourneys.objects.get(pk=workjourney_id)
    workjourney.delete()
    return HttpResponseRedirect('/workjourneys')

def edit(request, workjourney_id):
    workjourney = Workjourneys.objects.get(pk=workjourney_id)
    template = loader.get_template('workjourneys/edit.html')
    context = {
        'workjourney': workjourney,
    }
    return HttpResponse(template.render(context, request))

def edit_send(request, workjourney_id):
    workjourney = Workjourneys.objects.get(pk=workjourney_id)
    workjourney.name = request.POST['name']
    workjourney.code = request.POST['code']
    workjourney.schedule = request.POST['schedule']
    workjourney.save()
    return HttpResponseRedirect('/workjourneys/' + workjourney_id)
