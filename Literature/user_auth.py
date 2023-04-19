import base64
import binascii

from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from rest_framework import permissions
from rest_framework.authentication import BaseAuthentication, BasicAuthentication, get_authorization_header
from rest_framework.exceptions import AuthenticationFailed
# from Users.models import UserToken, UserInfo
from rest_framework import HTTP_HEADER_ENCODING, exceptions

from django.contrib import auth


# class MyTokenAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         print(request.data)
#         token = '3c2e5940-c07a-4223-a0e6-a141c8b12997'
#         if token:
#             user_token = UserToken.objects.filter(token=token).first()
#
#             if user_token:
#                 return user_token.user, token
#             else:
#                 raise AuthenticationFailed('认证失败')
#         else:
#             raise AuthenticationFailed('请求地址中需要携带Token')
#
#
# class MySessionAuthentication(BaseAuthentication):
#     def authenticate(self, request):
#         session = request.session['UserInfo']
#         print(session)
#         if session:
#
#             return session['id'], session['account']
#         else:
#             raise AuthenticationFailed('请登录用户后进行操作')
#

# class MyBasicAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         auth = get_authorization_header(request).split()
#
#         if not auth or auth[0].lower() != b'basic':
#             return None
#
#         if len(auth) == 1:
#             msg = _('Invalid basic header. No credentials provided.')
#             raise exceptions.AuthenticationFailed(msg)
#         elif len(auth) > 2:
#             msg = _('Invalid basic header. Credentials string should not contain spaces.')
#             raise exceptions.AuthenticationFailed(msg)
#
#         try:
#             try:
#                 auth_decoded = base64.b64decode(auth[1]).decode('utf-8')
#             except UnicodeDecodeError:
#                 auth_decoded = base64.b64decode(auth[1]).decode('latin-1')
#             auth_parts = auth_decoded.partition(':')
#         except (TypeError, UnicodeDecodeError, binascii.Error):
#             msg = _('Invalid basic header. Credentials not correctly base64 encoded.')
#             raise exceptions.AuthenticationFailed(msg)
#
#         userid, password = auth_parts[0], auth_parts[2]
#         user = UserInfo.objects.filter(account=userid, password=password).first()
#         print(userid, password, user)
#         if user:
#             return
#         else:
#             raise AuthenticationFailed('账号或密码不正确！')


class IsOwnerReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        所有的request请求都有读权限，因此一律允许GET/HEAD/OPTIONS方法
        :param request:
        :param view:
        :param obj:
        :return: bool
        """
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user == obj.author
