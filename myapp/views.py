from django.shortcuts import HttpResponse

def index(request):
    return HttpResponse('Hello!')

def acrticles(request):
    return HttpResponse('Hello acrticles!')

def archive(request):
    return HttpResponse('Hello! archive')

def users(request):
    return HttpResponse('users!')
