from django.urls import path

from bbsadmin.api.user.UserApiView import RegisterApi

app_name = 'user'

urlpatterns = [
    # 用户注册
    path('register', RegisterApi.as_view(), name='register'),
]
