from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.shortcuts import redirect
from django.contrib.auth.hashers import make_password, check_password

def login(request):
    context = {}
    if 'email' in request.session: # if exist session go board page
        return redirect('/board')

    return render(request, 'login/login.html', context)

def api_login(request):
    email = request.POST.get('email')
    password = make_password(request.POST.get('password'), 'steeljin','default')

    with connections['default'].cursor() as cur:
        query = '''
                SELECT count(*)
                FROM user 
                WHERE id='{email}' AND password='{password}';
                UPDATE user_login_attempt 
                SET attempt = attempt + 1, modify_date = now()
                WHERE user_id=((SELECT seq FROM user WHERE id='{email}'));
            '''.format(email=email, password=password)
        cur.execute(query)
        rows = cur.fetchall()

    if rows[0][0] != 0:
        request.session['email'] = email
        request.session.set_expiry(900)
        return JsonResponse({'result':'success'}) #session up

    return JsonResponse({'result':'false'})


def api_logout(request):
    try:
        del request.session['email']
    except KeyError:
        pass
    return JsonResponse({'result':'success'})

def api_regist(request):
    email = request.POST.get('email')
    password = make_password(request.POST.get('password'), 'steeljin','default')

# if 문으로 email및 password공백 일경우와 @이메일 형식 아닌 경우 등을 거르는 기능 필요.
# 또한 SQLinjection Filter만들것

    with connections['default'].cursor() as cur:
        query = '''
            INSERT INTO user(id, password) 
            VALUES ('{email}','{password}');
            INSERT INTO user_login_attempt(user_id)
            VALUES ((
                SELECT seq FROM user WHERE id='{email}'
            ));
        '''.format(email=email, password=password)
        cur.execute(query)

    return JsonResponse({'result':'success'})

def api_check(request):
    email = request.POST.get('email')

    with connections['default'].cursor() as cur:
        query = '''
                SELECT count(*)
                FROM user 
                WHERE id='{email}';
        '''.format(email=email)
        cur.execute(query)
        rows = cur.fetchall()

    if rows[0][0] != 0:
        return JsonResponse({'result': 'False'})

    return JsonResponse({'result': 'True'})
