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
# login_attempt 테이블을 회원가입할때 생성하고 시도 값 0로 주도록 만들어야함.
# 이후 로그인시 1씩 증가 및 현재시각으로 업데이트 시키면 될듯.
# 여기서 id가 동잃해야함.

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
