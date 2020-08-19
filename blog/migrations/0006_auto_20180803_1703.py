# Generated by Django 2.1 on 2018-08-03 15:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('blog', '0005_auto_20150702_1725'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-posted_on']},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ['-posted_on', '-pk']},
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                    to='blog.Post', verbose_name='Post'),
        ),
    ]