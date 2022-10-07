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
    # queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsPagination  # 自定义分页参数

    #  处理前端传递的参数
    def get_queryset(self):
        queryset = Goods.objects.all()
        # 初级版过滤查询: 查询前端传过来的参数字段price_min 值大于指定数值int(price_min) 的的数据列表
        price_min = self.request.query_params.get('price_min', 0)
        if price_min:
            queryset = queryset.filter(shop_price__gt=int(price_min))
        return queryset
