# -*- coding: utf-8 -*-

from django.db import models

from django.contrib.auth.hashers import make_password

from car_backend.libs import Validators

class CustomerAuth(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    type_choice = (
        ('P', 'Phone'),
        ('W', 'Weibo'),
        ('C', 'WeChat'),
        ('Q', 'QQ'),
    )
    identity_type = models.CharField(max_length=1, choices=type_choice, verbose_name='登录类型')
    identifier = models.CharField(max_length=100, verbose_name='用户名', unique=True)
    credential = models.CharField(max_length=250, verbose_name='密码')
    verified = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.credential:
            self.credential = make_password(self.credential, None, 'pbkdf2_sha256')
        super(CustomerAuth, self).save(force_insert, force_update, using, update_fields)

    class Meta:
        db_table = "customer_auth"
        get_latest_by = 'identity_type'
        verbose_name_plural = '客户认证'
        verbose_name = '客户认证'

    def __str__(self):
        return self.identifier


class CustomerInfo(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    phone = models.CharField(max_length=20,unique=True,null=True,blank=True,verbose_name='手机号',validators=[Validators.validate_phone])
    client_id = models.OneToOneField(CustomerAuth, on_delete=models.CASCADE,primary_key=True,verbose_name='客户id')
    nickname = models.CharField(max_length=20,null=True,blank=True,verbose_name='昵称')

    class Meta:
        db_table="customer_info"
        get_latest_by = 'created_at'
        ordering = ['created_at']
        verbose_name_plural='客户详情'
        verbose_name='客户详情'

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if not self.nickname:
            self.nickname = self.client_id.identifier
        super(CustomerInfo,self).save(force_insert,force_update,using,update_fields)

    def __unicode__(self):
        return self.nickname