from rest_framework import mixins
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend  # 未生效
# from django_filters import rest_framework as filter

from .models import Goods, GoodsCategory
from .filters import GoodsFilter  # 未生效
from .serializers import GoodsSerializer, CategorySerializer

from rest_framework.authentication import TokenAuthentication


class GoodsPagination(PageNumberPagination):
    page_size = 12
    page_size_query_param = 'page_size'
    page_query_param = "pagey"
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页: 分页，搜索，过滤，排序
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 自定义分页参数
    authentication_classes = (TokenAuthentication,)  # 局部配置token
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filterer_fields = GoodsFilter # filters.py 未生效
    # docs https://www.django-rest-framework.org/api-guide/filtering/#setting-filter-backends
    filterset_fields = ['shop_price', 'market_pri ce']  # 精确搜索
    search_fields = ('name', 'goods_brief', 'goods_desc')  # 同一个搜索内容，可查询三个字段中的内容
    ordering_fields = ['sold_num', 'shop_price']


class CategoryViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list
        商品分类列表数据
        可以进入其对应的详情页 mixins.RetrieveModelMixin
        测试入口 http://127.0.0.1:8000/categorys/24/ [第一层的id]
    """
    # queryset = GoodsCategory.objects.all()  # 获取数据库表中的所有数据
    queryset = GoodsCategory.objects.filter(category_type=1)  # 添加查询条件 category_type 字段值为 1 的数据

    serializer_class = CategorySerializer
