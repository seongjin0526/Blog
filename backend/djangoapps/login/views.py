from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect


def login(request):
    context = {}
    return render(request, 'login/login.html', context)
