from .serializers import GoodsSerializer

from rest_framework import mixins
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination

from .models import Goods


class GoodsPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    page_query_param = "pagey"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 自定义分页参数

"""
view 的继承关系 查看源码 generics.py -> from rest_framework import generics
GenericViewSet(viewSet)   -drf
    GenericAPIView        -drf    
        APIView           -drf  过滤功能，序列化，分页
            View          -django
            
mixin  查看源码 mixins.py -> from rest_framework import mixins
   CreateModelMixin
   ListModelMixin  分页功能
   UpdateModelMixin 部分更新还是全部更新
   RetrieveModelMixin
   DestroyModelMixin 删除操作，并返回指定的状态码
"""