from django.urls import path
from django.conf.urls import url, include

from .djangoapps.login import views as LoginViews
from .djangoapps.board import views as BoardViews

urlpatterns = [
    url('api_login$', LoginViews.api_login, name="api_login"),
    url('api_logout$', LoginViews.api_logout, name="api_logout"),
    url('api_regist', LoginViews.api_regist, name='api_regist'),
    url('api_email_check', LoginViews.api_email_check, name='api_email_check'),
    url('login$', LoginViews.login, name='login'),
    url('board$', BoardViews.board, name='board'),
    url('$', BoardViews.board, name='board'),

]
