# -*- coding: utf-8 -*-
__author__ = 'WenLong'

from rest_framework import serializers

from goods.models import Goods, GoodsCategory


class CategorySerializer3(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer2(serializers.ModelSerializer):
    sub_cat = CategorySerializer3(many=True)

    class Meta:
        model = GoodsCategory
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):
    """
    商品类别序列化
    """
    sub_cat = CategorySerializer2(many=True)  # 此字段与约定的数据表中的需 一致 可能有多个

    class Meta:
        model = GoodsCategory
        fields = "__all__"


# 高级版
class GoodsSerializer(serializers.ModelSerializer):
    category = CategorySerializer()  # 覆盖外健对应的字段表

    # images = GoodsImageSerializer(many=True)
    class Meta:
        model = Goods
        fields = "__all__"

# 初级版
# class GoodsSerializer(serializers.serializer):
#     name = serializers.CharField(required=True, max_length=100)
#     click_num = serializers.IntegerField(default=0)
#     goods_front_image = serializers.ImageField()
#
#     def create(self, validated_data):
#         """
#         Create and return a new ``
#         :param validated_data:
#         :return:
#         """
#         return Goods.objects.create(**validated_data)

# 中级版
# class GoodsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Goods
#         # fields = ('name', 'click_num', 'goods_front_image')  # 序列化指定的字段
#         fields = "__all__"  # 序列化所有的表格字段
