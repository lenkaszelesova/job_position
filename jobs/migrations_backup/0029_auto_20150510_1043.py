# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0028_auto_20150510_0858'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job_position',
            name='code',
        ),
        migrations.RemoveField(
            model_name='job_position',
            name='highlighted',
        ),
        migrations.RemoveField(
            model_name='job_position',
            name='language',
        ),
        migrations.RemoveField(
            model_name='job_position',
            name='linenos',
        ),
        migrations.RemoveField(
            model_name='job_position',
            name='style',
        ),
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 10, 10, 43, 47, 226572, tzinfo=utc), verbose_name=b'Job created'),
        ),
    ]
