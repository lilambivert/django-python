# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('book', models.CharField(max_length=250)),
                ('price', models.IntegerField()),
                ('address', models.CharField(max_length=250)),
                ('user', models.ForeignKey(related_name='user_info', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
