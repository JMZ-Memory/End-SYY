from django.db import models
from django.contrib.auth.models import AbstractUser


class UserInfo(AbstractUser):
    nickname = models.CharField(max_length=20, default='', verbose_name="昵称")
    icon = models.ImageField(upload_to='icon/', blank=True, verbose_name="头像")
    phone = models.CharField(max_length=32, blank=True, verbose_name="手机号")
    is_first_modify = models.BooleanField(verbose_name="是否第一次修改", default=False)
    gender = models.SmallIntegerField(choices=((1, '男'), (2, "女"), (3, "保密")), default=3, verbose_name="性别")
    birthday = models.DateTimeField(verbose_name="生日", null=True)
    signature = models.TextField(verbose_name="我的签名", null=True)

    class Meta(AbstractUser.Meta):
        pass
