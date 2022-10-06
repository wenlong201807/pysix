# -*- coding: utf-8 -*-
__author__ = 'WenLong'

from django.views.generic.base import View

from goods.models import Goods
# from django.views.generic import ListView


class GoodsListView(View):
    def get(self, request):
        """
        通过django的view实现商品列表页
        :param request:
        :return:
        """
        json_list = []
        goods = Goods.objects.all()[:10]

        # 第一种方式
        # for good in goods:
        #     json_dict = {}
        #     json_dict["name"] = good.name
        #     json_dict["category"] = good.category.name
        #     json_dict["market_price"] = good.market_price
        #     json_dict["add_time"] = good.add_time
        #     json_list.append(json_dict)

        # 第二种方式 有些字段 转化之后会有问题
        # from django.forms.models import model_to_dict
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)

        # 第三种方式
        import json
        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        json_data = json.loads(json_data)
        from django.http import HttpResponse, JsonResponse
        # return HttpResponse(json.dump(json_list), content_type="application/json")
        return JsonResponse(json_data, safe=False)



