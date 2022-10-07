from django.db import models

from tools.models.MyModel import BaseModel


class User(BaseModel):
    """
    用户
    """

    class BoolChoice:
        YES = True
        NO = False
        choice = (
            (YES, '是'),
            (NO, '否')
        )

    class SexChoices:
        MAN = 1
        WOMAN = 2

        choices = (
            (MAN, '男'),
            (WOMAN, '女'),
        )

    username = models.CharField(verbose_name='帐号', max_length=64)
    password = models.CharField(verbose_name='密码', max_length=256)
    name = models.CharField(verbose_name='姓名', max_length=80, null=True, blank=True)
    head_image = models.CharField(verbose_name='头像', max_length=1024, null=True, blank=True)
    sex = models.IntegerField(verbose_name='性别', choices=SexChoices.choices, null=True, blank=True)
    login_at = models.DateTimeField(verbose_name='最后登录时间', null=True, blank=True)
    disable = models.BooleanField(verbose_name='被禁用', default=BoolChoice.NO, choices=BoolChoice.choice)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'
