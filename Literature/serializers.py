from rest_framework import serializers
from Literature.models import Literature, Novel, Modern_Poetry, Ancient_Poetry, NovelChapter
from django.contrib.auth import get_user_model


# 文学类型
class LiteratureSerializers(serializers.ModelSerializer):
    class Meta:
        model = Literature
        fields = '__all__'

    def create(self, validated_data):
        new_book = Literature.objects.create(**self.validated_data)
        return new_book

    def update(self, instance, validated_data):
        Literature.objects.filter(pk=instance.pk).update(**self.validated_data)
        updated_book = Literature.objects.get(pk=instance.pk)
        return updated_book


# 现代诗序列化
class LiteratureModernSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname', default='无名氏')

    class Meta:
        model = Modern_Poetry
        fields = '__all__'

    def update(self, instance, validated_data):
        Modern_Poetry.objects.filter(pk=instance.pk).update(**self.validated_data)
        new_poetry = Modern_Poetry.objects.get(pk=instance.pk)
        return new_poetry


# 古诗词序列化
class LiteratureAncientSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname', default='无名氏')

    class Meta:
        model = Ancient_Poetry
        fields = '__all__'

    def update(self, instance, validated_data):
        Ancient_Poetry.objects.filter(pk=instance.pk).update(**self.validated_data)
        new_poetry = Ancient_Poetry.objects.get(pk=instance.pk)
        return new_poetry


# 小说
class NovelSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname', default='无名氏')

    class Meta:
        model = Novel
        fields = '__all__'

    def update(self, instance, validated_data):
        Novel.objects.filter(pk=instance.pk).update(**self.validated_data)
        updated_book = Novel.objects.get(pk=instance.pk)
        return updated_book


# 小说章节
class NovelChapterSerializers(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.nickname', default='无名氏')
    novel_name = serializers.ReadOnlyField(source='Novel.name')

    class Meta:
        model = NovelChapter
        filter = '__all__'

    def update(self, instance, validated_data):
        NovelChapter.objects.filter(pk=instance.pk).update(**self.validated_data)
        updated_book = NovelChapter.objects.get(pk=instance.pk)
        return updated_book
