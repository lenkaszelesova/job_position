# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0010_auto_20150509_1455'),
    ]

    operations = [
        migrations.AddField(
            model_name='job_position',
            name='code',
            field=models.TextField(default='Job'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 9, 14, 57, 48, 135765, tzinfo=utc), verbose_name=b'Job created'),
        ),
    ]
