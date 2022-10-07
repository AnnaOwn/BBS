from django.db import models

from bbsadmin.models.UserModel import User
from tools.models.MyModel import BaseModel


class ArticleClassify(BaseModel):
    """
    文章分类
    """
    parent = models.ForeignKey('ArticleClassify', verbose_name='父级', null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名称', max_length=64)
    sort_code = models.IntegerField(verbose_name='排序', default=999)


class Article(BaseModel):
    """
    文章
    """
    article_classify = models.ForeignKey(ArticleClassify, verbose_name='分类', on_delete=models.CASCADE)
    name = models.CharField(verbose_name='名称', max_length=64)
    content = models.TextField(verbose_name='内容')


class Comment(BaseModel):
    """
    评论
    """
    article = models.ForeignKey(Article, verbose_name='文章', on_delete=models.CASCADE)
    user = models.ForeignKey(User, verbose_name='用户', on_delete=models.CASCADE)
    reply = models.ForeignKey('Comment', verbose_name='回复的评论', null=True, blank=True, on_delete=models.CASCADE)
    content = models.CharField(verbose_name='内容', max_length=256)
