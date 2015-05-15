# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0006_auto_20150508_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 8, 15, 35, 58, 452495, tzinfo=utc), verbose_name=b'Job created'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='language_requirements',
            field=models.CharField(max_length=20, verbose_name=b'Language requirements', choices=[(b'EN-1', b'English - basic'), (b'English - advanced', b'English advanced'), (b'DE-1', b'German - basic'), (b'DE-2', b'German - advanced')]),
        ),
    ]
