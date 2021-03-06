# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-10 11:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20161210_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='user_group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.UserGroup'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='password',
            field=models.CharField(help_text='pwd', max_length=60),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='test',
            field=models.EmailField(error_messages={'invalid': '请输入密码'}, max_length=19, null=True),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='username',
            field=models.CharField(blank=True, max_length=32, verbose_name='用户名'),
        ),
    ]
