# Generated by Django 4.1.7 on 2023-03-14 10:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Literature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('literature_type', models.CharField(help_text='类型名称', max_length=32, verbose_name='类型')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
        ),
        migrations.CreateModel(
            name='Novel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='书籍名称', max_length=32, verbose_name='书名')),
                ('img', models.ImageField(upload_to='', verbose_name='封面')),
                ('synopsis', models.TextField(verbose_name='简介')),
                ('create_time', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('literature_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Literature.literature', verbose_name='类型')),
            ],
        ),
        migrations.CreateModel(
            name='Chapter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateField(auto_created=True)),
                ('name', models.CharField(help_text='章节名称', max_length=32, verbose_name='章节名称')),
                ('context', models.TextField(verbose_name='内容')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
                ('novel_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Literature.novel', verbose_name='书名')),
            ],
        ),
    ]
