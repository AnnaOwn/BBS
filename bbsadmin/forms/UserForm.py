from django import forms


class RegisterForm(forms.Form):
    """用户注册表单"""
    username = forms.CharField(label='帐号')
    password = forms.CharField(label='密码')
    name = forms.CharField(label='姓名', required=False)
    head_image = forms.CharField(label='头像', required=False)
    sex = forms.IntegerField(label='性别', required=False)
