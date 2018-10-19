from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections
from django.shortcuts import redirect

def board(request):
    context = {}
    if 'email' not in request.session:
        return redirect('/login')
    else:
        email = request.session['email'] # check Session

    context['email'] = email
    return render(request, 'board/board.html', context)