from django.http import HttpResponse
from django.views import View

from tools.biz.response import StatusCode, response_json_message


class BaseApiView(View):
    """
    base api
    """

    def options(self, request, *args, **kwargs):
        """Handle responding to requests for the OPTIONS HTTP verb."""
        response = HttpResponse()
        response['Allow'] = ', '.join(self._allowed_methods())
        response['Content-Length'] = '0'
        response["Access-Control-Allow-Credentials"] = 'true'
        response["Access-Control-Allow-Origin"] = "*"
        response['Access-Control-Request-Headers'] = 'presetproperties'
        response["Access-Control-Allow-Methods"] = "POST, GET"
        # response["Access-Control-Max-Age"] = "1000"
        response["Access-Control-Allow-Headers"] = "*"
        return response

    @classmethod
    def get_response(cls, request, code, data=None, message=None):
        """
        消息处理
        """
        if code == StatusCode.NeedLoginError:
            response = response_json_message(request, code)
        else:
            response = response_json_message(request, code, data, message)
        return response


class UserTokenApiView(BaseApiView):
    """
    user token api
    """
