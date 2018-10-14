from django.urls import path
from django.conf.urls import url, include

from .djangoapps.login import views as LoginViews
from .djangoapps.board import views as BoardViews

urlpatterns = [
    url('api_login$', LoginViews.api_login, name="api_login"),
    url('api_regist', LoginViews.api_regist, name='api_regist'),
    url('login$', LoginViews.login, name='login'),
    url('board$', BoardViews.login, name='board'),

]
