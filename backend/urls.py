from django.urls import path
from django.conf.urls import url, include

from .djangoapps.login import views as LoginViews

urlpatterns = [
    url('login$', LoginViews.login, name='login'),
]
