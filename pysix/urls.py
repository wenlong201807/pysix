"""pysix URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import defaults
# from django.urls import path
from django.urls import include, re_path
# from django.urls import re_path as url
import xadmin

from pysix.settings import MEDIA_ROOT
from django.views.static import serve
from rest_framework.documentation import include_docs_urls

from goods.views_base import GoodsListView

urlpatterns = [
    # re_path('xadmin/', xadmin.site.urls),
    re_path(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    # 图片访问路径 没有成功
    # testUrl: http://127.0.0.1:8000/media/banner/banner1.jpg
    # 成功 testUrl: http://127.0.0.1:8000/media/goods/images/2_20170719161405_249.jpg
    re_path(r'^media/(?P<path>.*)$', serve, {"document_root": MEDIA_ROOT}),

    # 测试访问 http://127.0.0.1:8000/goods/
    re_path(r'goods/$', GoodsListView.as_view(), name="goods-list"),

    # api文档地址
    re_path(r'docs/', include_docs_urls(title='py接口文档')),
]
