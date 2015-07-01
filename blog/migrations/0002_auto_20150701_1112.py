# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(verbose_name='Category', max_length=255)),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.SlugField(verbose_name='Slug', default='a'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_by',
            field=models.ForeignKey(verbose_name='Posted by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='post',
            name='posted_on',
            field=models.DateTimeField(verbose_name='Posted on', auto_now_add=True),
        ),
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.ManyToManyField(verbose_name='Categories', to='blog.Category'),
        ),
    ]
