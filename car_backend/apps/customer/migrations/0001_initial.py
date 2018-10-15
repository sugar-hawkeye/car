# Generated by Django 2.1.2 on 2018-10-14 13:55

import car_backend.libs.Validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerAuth',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('identity_type', models.CharField(choices=[('P', 'Phone'), ('W', 'Weibo'), ('C', 'WeChat'), ('Q', 'QQ')], max_length=1, verbose_name='登录类型')),
                ('identifier', models.CharField(max_length=100, unique=True, verbose_name='用户名')),
                ('credential', models.CharField(max_length=250, verbose_name='密码')),
                ('verified', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': '客户认证',
                'verbose_name_plural': '客户认证',
                'db_table': 'customer_auth',
                'get_latest_by': 'identity_type',
            },
        ),
        migrations.CreateModel(
            name='CustomerInfo',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('edited_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(blank=True, max_length=20, null=True, unique=True, validators=[car_backend.libs.Validators.validate_phone], verbose_name='手机号')),
                ('client_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='customer.CustomerAuth', verbose_name='客户id')),
                ('nickname', models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称')),
            ],
            options={
                'verbose_name': '客户详情',
                'verbose_name_plural': '客户详情',
                'db_table': 'customer_info',
                'ordering': ['created_at'],
                'get_latest_by': 'created_at',
            },
        ),
    ]
