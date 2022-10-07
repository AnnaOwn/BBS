from django.contrib.auth.hashers import make_password, check_password

from bbsadmin.models.UserModel import User


class UserBiz:
    """
    用户操作流程代码
    """

    @classmethod
    def register(cls, cleaned_data):
        """用户注册"""
        username = cleaned_data.get('username')
        cleaned_data['password'] = make_password(cleaned_data['password'])
        if User.objects.filter(username=username):
            raise Exception(f'用户名: {username}已被使用!')
        User.objects.create(**cleaned_data)
