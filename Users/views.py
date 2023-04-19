import random
import uuid
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from django.core.mail import send_mail
from django.shortcuts import render, HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from Users.mixins import encrypt
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
# from django.contrib.auth.models import User

from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from Users import serializers
from Users.models import UserInfo


def test(request):
    if request.method == "GET":
        return render(request, 'text.html')
    if request.method == "POST":
        subject = "思叶云"
        message = """
        hello!我是谁？我是谁？<a href="https://www.baidu.com">百度一下</a>
        """
        emails = "2549626703@qq.com"
        result = send_mail(subject=subject, message="", html_message=message, from_email=settings.EMAIL_HOST_USER,
                           recipient_list=[emails])
        print(result)
        return HttpResponse('ok')


@csrf_exempt
@api_view(["POST"])
def email_check(request):
    if request.method == "POST":
        emails = request.data['email']
        code = []
        for i in range(5):
            num = str(random.randint(0, 9))
            code.append(num)
        code = "".join(code)
        subject = "思叶云"
        message = """
            【验证码】:{},思叶云用户验证,请勿随意转发，验证码仅在三分钟内有效，请用户及时操作，
            """.format(code)
        try:
            send_mail(subject=subject, message="", html_message=message, from_email=settings.EMAIL_HOST_USER,
                      recipient_list=[emails])
            return Response(status=status.HTTP_200_OK, data=code)
        finally:
            return Response(status=status.HTTP_200_OK, data="此邮箱并未注册")


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def generate_token(sender, instance=None, created=False, **kwargs):
    """创建用户时自动生成Token"""
    if created:
        Token.objects.update_or_create(user=instance)


@csrf_exempt
@api_view(["POST"])
def login_view(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        if UserInfo.objects.filter(email=username).exists():
            request.data['username'] = UserInfo.objects.filter(email=username).first().username
        elif UserInfo.objects.filter(phone=username).exists():
            request.data['username'] = UserInfo.objects.filter(phone=username).first().username
        elif UserInfo.objects.filter(username=username).exists():
            pass
        else:
            return Response(status=status.HTTP_404_NOT_FOUND, data={"msg": "账号不存在"})
        user = authenticate(username=request.data['username'], password=password)
        if user:
            login(request, user)
            pk = request.user.pk
            print(request.session)
            return Response(status=status.HTTP_200_OK,
                            data={'token': Token.objects.filter(user_id=pk).first().key, 'session': request.session})
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data={"msg": "密码错误"})


@api_view(["GET"])
def logout_view(request):
    logout(request)
    return Response(status.HTTP_200_OK, status=status.HTTP_200_OK)


@csrf_exempt
@api_view(["POST"])
def register(request):
    if request.method == 'POST':
        username = request.data['username']
        password = request.data['password']
        request.data['password'] = make_password(password)
        if "@" in username:
            request.data["email"] = username
        else:
            request.data["phone"] = username
        request.data['username'] = str(uuid.uuid4()).replace('-', '')
        serializer = serializers.UserSerializer(data=request.data)
        if serializer.is_valid():
            if UserInfo.objects.filter(username=username).exists():
                return Response(status=status.HTTP_400_BAD_REQUEST)
            else:
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@method_decorator(csrf_exempt, name='dispatch')
class UserList(APIView):
    # authentication_classes = [MyTokenAuthentication]

    # permission_classes = [IsOwnerReadOnly]

    @staticmethod
    def get_object(pk):
        print(Token.objects.filter(token=pk).first().user_id)
        pk = Token.objects.filter(token=pk).first().user_id
        print(pk)
        try:
            return UserInfo.objects.get(id=pk)
        except UserInfo.DoesNotExist:
            print(Token.objects.filter(token=pk).first().user_id)
            return

    def get(self, request, pk):
        user = self.get_object(pk=pk)
        serializer = serializers.UserSerializer(instance=user, many=False)
        return Response(serializer.data)

    def put(self, request, pk):
        user = self.get_object(pk=pk)
        request.data['password'] = encrypt.md5(request.data['password'])
        serializer = serializers.UserSerializer(instance=user, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)


@method_decorator(csrf_exempt, name='dispatch')
class UserDetailView(APIView):
    # authentication_classes = [BasicAuthentication, TokenAuthentication,SessionAuthentication]

    # permission_classes = [IsOwnerReadOnly]

    # @staticmethod
    # def get_object(pk):
    #     pk = Token.objects.filter(key=pk).first().user_id
    #     try:
    #         return UserInfo.objects.get(pk=Token.objects.filter(key=pk).first().user_id)
    #     except UserInfo.DoesNotExist:
    #         return

    def get(self, request, pk):
        if Token.objects.filter(key=pk).exists():
            print(request.auth)
            print(request.user.is_active)
            print(request.user)
            print(request.session)
            # print(request.session['UserInfo']['id'])
            user = UserInfo.objects.get(pk=Token.objects.filter(key=pk).first().user_id)
            serializer = serializers.UserDetailSerializer(instance=user, many=False)
            return Response(serializer.data)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        print(request.user)
        print(request.auth)
        if Token.objects.filter(key=pk).exists():
            user = UserInfo.objects.get(pk=Token.objects.filter(key=pk).first().user_id)
            serializer = serializers.UserDetailSerializer(instance=user, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status.HTTP_404_NOT_FOUND)

    # def delete(self, request, pk):
    #     obj = self.get_object(pk=pk)
    #     if not obj:
    #         return Response(data={"msg": "删除失败"}, status=status.HTTP_404_NOT_FOUND)
    #     obj.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
