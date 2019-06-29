from django.db import models
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib import admin


# Create your models here.
"""
# 图书管理器
class BookInfoManager(models.Manager):
    def all(self):
        # 默认查询未删除的图书信息
        # 调用父类的成员语法为：super().方法名
        return super().filter(is_delete=False)
    def create_book(self, title, pub_data):
        # 创建模型类对象self.model可以获得模型类
        book = self.model()
        book.btitle = title 
        book.bpub_data = pub_data
        book.bread = 0
        book.bcomment = 0
        book.is_delete = False
        # 将数据插入进数据表
        book.save()
        return book
""" 


# 定义图书模型类BookInfo
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20, verbose_name='名称')
    bpub_data = models.DateField(verbose_name='发布日期')
    bread = models.IntegerField(default=0, verbose_name='阅读量')
    bcomment = models.IntegerField(default=0, verbose_name='评论量')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    # books = BookInfoManager() 
    image = models.ImageField(upload_to = 'Users', verbose_name = '图片', null = True)

    def pub_date(self):
        return self.bpub_data.strftime("%Y年%m月%d日")
        # 设置方法字段在admin中显示的标题
    pub_date.short_description = '发布日期'


    class Meta:
        # 指明数据库表名
        db_table = 'tb_books'
        # 在admin站点中显示的名称
        verbose_name = '图书'
        # 显示的复数名称
        verbose_name_plural = verbose_name

    def __str__(self):
        """定义每个数据对象的显示信息"""
        return self.btitle
    
    
# 定义影响模型类HeroInfo
class HeroInfo(models.Model):
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    hname = models.CharField(max_length=20, verbose_name='姓名')
    hgender = models.SmallIntegerField(choices=GENDER_CHOICES, default=0, verbose_name='性别')
    hcomment = models.CharField(max_length=200, null=True, verbose_name='描述信息')
    hbook = models.ForeignKey(BookInfo, on_delete=models.CASCADE, verbose_name='图书')
    is_delete = models.BooleanField(default=False, verbose_name='逻辑删除')
    
    def read(self):
        return self.hbook.bread
    read.short_description = '图书阅读量'


    class Meta:
        db_table = 'tb_heros'
        verbose_name = '英雄'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.hname 


def get_sentinel_user():
    return get_user_model().object.get_or_create(username='delete')[0]


class MyModel(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET(get_sentinel_user),
    )























