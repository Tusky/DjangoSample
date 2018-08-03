# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0004_post_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Comment')),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AlterField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Active'),
        ),
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(to='blog.Post', verbose_name='comments', on_delete=models.CASCADE),
        ),
        migrations.AddField(
            model_name='comment',
            name='posted_by',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL, verbose_name='Posted by', on_delete=models.PROTECT),
        ),
    ]
