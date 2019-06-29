#!/usr/bin/env python
# coding=utf-8
from rest_framework import serializers
from .models import BookInfo, HeroInfo


def about_django(value):
    if 'django' not in value.lower():
        raise serializers.ValidationError('不是Django')



class BookInfoSerializer(serializers.Serializer):
    """图书数据序列化器"""
    id= serializers.IntegerField(label='ID', read_only=True)
    btitle = serializers.CharField(label='名称', max_length=20)
    bpub_date = serializers.DateField(label='发布日期', required=False)
    bread = serializers.IntegerField(label='阅读量', required=False)
    bcomment = serializers.IntegerField(label='评论量', required=False)
    image = serializers.ImageField(label='图片', required=False)
    heroinfo_set = serializers.PrimaryKeyRelatedField(read_only=True, many=True)  # 新增

    def validate_btitle(self, value):
        if 'django' not in value.lower():
            raise serializers.ValidationError('图书不是关于Django的')
        return value

    def validate(self, attrs):
        bread = attrs['bread']
        bcomment = attrs['bcomment']
        if bread < bcomment:
            raise serializers.ValidationError('阅读量小于评论量')
        return attrs



class HeroInfoSerializer(serializers.Serializer):
    """英雄数据序列化器"""
    GENDER_CHOICES = (
        (0, 'male'),
        (1, 'female')
    )
    id = serializers.IntegerField(label='ID', read_only=True)
    hname = serializers.CharField(label='名字', max_length=20)
    hgender = serializers.ChoiceField(choices=GENDER_CHOICES, label='性别', required=False)
    hcomment = serializers.CharField(label='描述信息', max_length=200, required=False, allow_null=True)
    # hbook = serializers.PrimaryKeyRelatedField(label='图书', queryset=BookInfo.objects.all())
    hbook = serializers.StringRelatedField(label='图书')
    # hbook = serializers.HyperlinkedRelatedField(label='图书', read_only=True, view_name='book-details')
    

class BookRelateField(serializers.RelatedField):
    """自定义用于处理图书的字段"""
    def to_presentation(self, value):
        return 'Book: %d %s' % (value.id, Value.btitle)


























