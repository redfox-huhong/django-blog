# Generated by Django 3.2.8 on 2021-10-25 13:27

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
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='标签')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否激活')),
            ],
            options={
                'verbose_name': '标签管理',
                'verbose_name_plural': '标签管理',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='文章类型')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否激活')),
            ],
            options={
                'verbose_name': '类型列表',
                'verbose_name_plural': '类型列表',
                'ordering': ['pk'],
            },
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='文章标题')),
                ('content', models.TextField(verbose_name='文章内容')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('view_count', models.IntegerField(default=0, verbose_name='浏览次数')),
                ('comment_count', models.IntegerField(default=0, verbose_name='评论数')),
                ('like_count', models.IntegerField(default=0, verbose_name='点赞数')),
                ('isActive', models.BooleanField(default=True, verbose_name='是否激活')),
                ('tags', models.ManyToManyField(to='blog.Tag', verbose_name='标签')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='blog.type', verbose_name='文章类型')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='作者')),
            ],
            options={
                'verbose_name': '文章列表',
                'verbose_name_plural': '文章列表',
            },
        ),
    ]
