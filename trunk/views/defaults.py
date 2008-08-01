from django import http
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def page_not_found(request, template_name='admin/404.html'):
    return render_to_response(template_name, {'request_path': request.path})

def server_error(request, template_name='admin/500.html'):
    return render_to_response(template_name)

def index(request):
    return render_to_response('index/index.html', {'user': request.user})
