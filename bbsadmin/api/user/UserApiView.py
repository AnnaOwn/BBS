import json

from bbsadmin.biz.user.UserBiz import UserBiz
from bbsadmin.forms.UserForm import *
from tools.api.MyApi import BaseApiView
from tools.biz.response import StatusCode


class RegisterApi(BaseApiView):
    """
    用户注册
    """

    def post(self, request, *args, **kwargs):
        try:
            if not request.body:
                raise Exception('未传递参数!')
            json_data = json.loads(request.body.decode())
            form = RegisterForm(json_data)
            if not form.is_valid():
                raise Exception(form.errors)
            UserBiz.register(form.cleaned_data)
            return self.get_response(request, StatusCode.OK)

        except Exception as e:
            return self.get_response(request, StatusCode.ValidError, message=e.args)
