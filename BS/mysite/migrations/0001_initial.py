# Generated by Django 3.0.4 on 2020-04-05 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='用户ID')),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='用户名')),
                ('telephone', models.IntegerField(max_length=20, verbose_name='手机号')),
                ('sfzid', models.CharField(max_length=50, verbose_name='身份证')),
                ('userpwd', models.CharField(max_length=50, verbose_name='密码')),
            ],
            options={
                'verbose_name': '用户信息表',
                'verbose_name_plural': '用户信息表',
            },
        ),
    ]
