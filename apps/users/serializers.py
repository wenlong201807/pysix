# -*- coding: utf-8 -*-
__author__ = 'WenLong'

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    '''
    token验证
    '''
    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['access'] = str(refresh.access_token)
        data['username'] = self.user.username #这个是你的自定义返回的
        data['user_id'] = self.user.id #这个是你的自定义返回的

        return data
#
# 作者：Itlaity
# 链接：https://juejin.cn/post/7091236896872857614
# 来源：稀土掘金
# 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。