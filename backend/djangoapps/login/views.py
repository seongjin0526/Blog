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

# if 문 및 delete 칼럼확인하여 로그인하도록 만들어야함.
# 로그인시 로그인 시도 테이블에 로그인 시도 로그 띄우도록 만들어야함.

    with connections['default'].cursor() as cur:
        query = '''
                SELECT count(*)
                FROM user 
                WHERE id='{email}' AND password='{password}'
            '''.format(email=email, password=password)
        cur.execute(query)
        rows = cur.fetchall()

    if rows[0][0] != 0:
        request.session['email'] = email
        return JsonResponse({'result':'success'}) #session up

    return JsonResponse({'result':'false'})

def api_regist(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

# if 문으로 email및 password공백 일경우와 @이메일 형식 아닌 경우 등을 거르는 기능 필요.

    with connections['default'].cursor() as cur:
        query = '''
            INSERT INTO user(id, password) 
            VALUES ('{email}','{password}');
        '''.format(email=email, password=password)
        cur.execute(query)

    return JsonResponse({'result':'success'})
