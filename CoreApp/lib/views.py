from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def login(request):
    template = loader.get_template('login/index.html')
    return HttpResponse(template.render({}, request))

def core_plug(request):
    template = loader.get_template('react_plug/index.html')
    return HttpResponse(template.render({}, request))