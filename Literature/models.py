from django.db import models


# Create your models here.
class Literature(models.Model):
    literature_type = models.CharField(verbose_name='类型', max_length=32, help_text='类型名称')


# 小说
class Novel(models.Model):
    name = models.CharField(max_length=32, verbose_name='书名', help_text='书籍名称')
    cover = models.GenericIPAddressField(verbose_name='封面')
    synopsis = models.TextField(verbose_name='简介')
    create_time = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to='Users.UserInfo', verbose_name='作者', to_field='id', on_delete=models.CASCADE)


# 小说章节
class NovelChapter(models.Model):
    name = models.CharField(max_length=32, verbose_name='章节名称', help_text='章节名称')
    context = models.TextField(verbose_name='内容')
    create_time = models.DateField(auto_created=True)
    novel_name = models.ForeignKey(to='Novel', verbose_name='书名', to_field='id', on_delete=models.CASCADE)
    author = models.ForeignKey(to='Users.UserInfo', verbose_name='作者', to_field='id', on_delete=models.CASCADE)


# 古诗词
class Ancient_Poetry(models.Model):
    title = models.CharField(max_length=32, verbose_name='题目')
    context = models.TextField(verbose_name='内容')
    create_time = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to='Users.UserInfo', verbose_name='作者', to_field='id', on_delete=models.CASCADE)


# 现代诗
class Modern_Poetry(models.Model):
    title = models.CharField(max_length=32, verbose_name='题目')
    context = models.TextField(verbose_name='内容')
    create_time = models.DateField(auto_now_add=True)
    author = models.ForeignKey(to='Users.UserInfo', verbose_name='作者', to_field='id', on_delete=models.CASCADE)
