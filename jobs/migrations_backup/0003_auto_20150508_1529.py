# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20150508_1451'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='contract_type',
            field=models.CharField(default=b'Full time', max_length=20, verbose_name=b'Contract type:', choices=[(b'FT', b'Full time'), (b'PT', b'Part time')]),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 8, 15, 29, 59, 923564, tzinfo=utc), verbose_name=b'Job created'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='job_requirements',
            field=models.CharField(default=b'University 2nd degree', max_length=20, verbose_name=b'Requirements', choices=[(b'1', b'University 1st degree'), (b'2', b'University 2nd degree'), (b'3', b'University 3rd degree')]),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='language_requirements',
            field=models.CharField(default=b'English - advanced', max_length=20, verbose_name=b'Language requirements', choices=[(b'EN-1', b'English - basic'), (b'EN-2', b'English - advanced'), (b'DE-1', b'German - basic'), (b'DE-2', b'German - advanced')]),
        ),
    ]
