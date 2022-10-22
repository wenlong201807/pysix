from rest_framework import viewsets, permissions
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework_simplejwt.views import TokenViewBase
from rest_framework_simplejwt.serializers import TokenRefreshSerializer

from user_operation.models import User
from .serializers import *
from .models import *


class MyTokenObtainPairView:
    """
    自定义得到token username: 账号或者密码 password: 密码或者验证码
    """
    serializer_class = MyTokenObtainPairSerializer


class MyTokenRefreshView(TokenViewBase):
    """
    自定义刷新token refresh: 刷新token的元素
    """
    serializer_class = TokenRefreshSerializer


class UserSerializer:
    pass


class UserViewSet(CacheResponseMixin, viewsets.ModelViewSet):
    """
    测试的Api1
    """
    permission_classes = [permissions.IsAuthenticated]  # 权限认证主要是这个
    queryset = User.objects.all()
    print(queryset)
    serializer_class = UserSerializer
    throttle_classes = []

# 作者：Itlaity
# 链接：https://juejin.cn/post/7091236896872857614
# 来源：稀土掘金
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。