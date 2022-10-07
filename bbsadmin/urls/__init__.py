from django.urls import path, include

app_name = 'bbs'

urlpatterns = [
    path('user/', include('bbsadmin.urls.url_user'))
]
