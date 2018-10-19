from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db import connections
from django.shortcuts import redirect

def login(request):
    context = {}
    if 'email' in request.session: # if exist session go board page
        return redirect('/board')

    return render(request, 'login/login.html', context)

def api_login(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

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
        return JsonResponse({'result':'success'}) #session up

    return JsonResponse({'result':'false'})

def api_regist(request):
    email = request.POST.get('email')
    password = request.POST.get('password')

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


# *sha256 길이 = 64자리, salt줘야함,
# login 후 세션 생성 및 세션 체크하도록 만들 것.