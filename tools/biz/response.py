from django.http import HttpRequest, JsonResponse


class StatusCode:
    """
    请求状态码
    """
    ValidError = (1001, '校验失败')
    KeyError = (1002, '键错误')
    ValueError = (1003, '值错误')
    TypeError = (1004, '类型错误')
    FileNameNoneError = (1005, '无文件名错误')
    PostCommanderError = (1006, '发送命令出错')
    LoginError = (1007, '登录失败')
    UserRepeatError = (1008, '用户重复')
    UserDeleteMeError = (1009, '删除自己')
    UserPermissionError = (1010, '权限不支持')
    ExecuteError = (1011, '执行出错')
    Waiting = (1012, '等待中')
    #
    PermissionError = (1100, '没有权限')
    RedirectError = (1200, '重定向')
    NeedLoginError = (1300, '需要登录')
    #
    OK = (0, 'ok')

    @classmethod
    def to_json(cls, code):
        try:
            return dict(code=code[0], message=code[1])
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(f'状态码定义错误: {e}')


def get_json_message(code, data=None):
    """
    获取json格式的回复数据
    """
    res = StatusCode.to_json(code)
    if data is not None:
        res['data'] = data
    return res


def response_json(data, request: HttpRequest = None):
    """
    允许跨站访问
    """
    origin = request.META.get('HTTP_ORIGIN') if (
            request is not None and request.META.get('HTTP_ORIGIN') is not None) else '*'
    response = JsonResponse(data, safe=False)
    response["Access-Control-Allow-Credentials"] = 'true'
    response["Access-Control-Allow-Origin"] = origin
    response['Access-Control-Request-Headers'] = 'presetproperties'
    response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    response[
        "Access-Control-Allow-Headers"] = "Origin, No-Cache, X-Requested-With, If-Modified-Since, Pragma, Last-Modified, Cache-Control, Expires, Content-Type, X-E4M-With"

    return response


def response_json_message(request, code, data=None, message=None):
    """
    返回json数据
    """
    data = get_json_message(code, data)
    if message:
        data['message'] = message
    return response_json(data, request)
