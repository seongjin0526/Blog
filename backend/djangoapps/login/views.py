from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

def login(request):
    context = {}
    return render(request, 'login/login.html', context)

def api_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

    print(email, password)

    with connections['default'].cursor() as cur:
        query = '''
                SELECT count(*)
                FROM user 
                WHERE id='{email}' AND password='{password}'
            '''.format(email=email, password=password)
        print(query)
        cur.execute(query)
        rows = cur.fetchall()
        print(rows)

    if rows[0][0] != 0:
        request.session['email'] = email
        return JsonResponse({'result':'success'}) #session up

    return JsonResponse({'result':'false'})

def api_regist(request):
    context= {}
    query = '''
            INSERT INTO user(id, password) VALUES ('email','passw')
    '''
    return JsonResponse({'test':'test'})