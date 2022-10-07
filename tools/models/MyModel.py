from django.db import models


class BaseModel(models.Model):
    """
    基础模型
    """
    create_at = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    update_at = models.DateTimeField(verbose_name='更新时间', auto_now=True)

    class Meta:
        abstract = True
