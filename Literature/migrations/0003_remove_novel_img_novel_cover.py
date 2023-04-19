# Generated by Django 4.1.7 on 2023-03-14 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Literature', '0002_rename_chapter_novelchapter'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='novel',
            name='img',
        ),
        migrations.AddField(
            model_name='novel',
            name='cover',
            field=models.ImageField(default='NovelCover/moren.png', upload_to='NovelCover/', verbose_name='封面'),
        ),
    ]
