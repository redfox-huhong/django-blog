from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签')
    isActive = models.BooleanField(default=True, verbose_name='是否激活')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = '标签管理'
        verbose_name_plural = '标签管理'

        ordering = ["pk"]

class Type(models.Model):
    name = models.CharField(max_length=20, verbose_name='文章类型')
    isActive = models.BooleanField(default=True, verbose_name='是否激活')

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = '类型列表'
        verbose_name_plural = '类型列表'

        ordering = ['pk']
    
class Article(models.Model):
    """ Article Model """
    title = models.CharField(max_length=50, null=False, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    type = models.ForeignKey(Type, on_delete=models.DO_NOTHING, verbose_name='文章类型')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='发布时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    view_count = models.IntegerField(default=0, verbose_name='浏览次数')
    comment_count = models.IntegerField(default=0, verbose_name='评论数')
    like_count = models.IntegerField(default=0, verbose_name='点赞数')
    tags = models.ManyToManyField(Tag, verbose_name='标签')
    isActive = models.BooleanField(default=True, verbose_name='是否激活')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = '文章列表'
        verbose_name_plural = '文章列表'