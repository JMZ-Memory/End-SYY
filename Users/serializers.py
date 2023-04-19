from rest_framework import serializers
from .models import UserInfo
from django.contrib.auth import get_user_model

User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "password", "email", "phone"]

    def create(self, validated_data):
        new_user = UserInfo.objects.create(**self.validated_data)
        return new_user

    def update(self, instance, validated_data):
        UserInfo.objects.filter(pk=instance.pk).update(**self.validated_data)
        updated_user = UserInfo.objects.get(pk=instance.pk)
        return updated_user


class UserDetailSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField()

    class Meta:
        model = User
        fields = ['nickname', 'gender', 'birthday', 'signature', 'username']

    def create(self, validated_data):
        new_user = UserInfo.objects.create(**self.validated_data)
        return new_user

    def update(self, instance, validated_data):
        UserInfo.objects.filter(pk=instance.pk).update(**self.validated_data)
        updated_user = UserInfo.objects.get(pk=instance.pk)
        return updated_user
