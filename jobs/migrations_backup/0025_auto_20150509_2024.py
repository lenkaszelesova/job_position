# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0024_auto_20150509_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='contract_type',
            field=models.CharField(default=b'Full time', max_length=20, verbose_name=b'Contract type:', choices=[(b'Full time', b'FT'), (b'Part time', b'PT')]),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 9, 20, 24, 35, 256745, tzinfo=utc), verbose_name=b'Job created'),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='job_requirements',
            field=models.CharField(default=b'University 2nd degree', max_length=20, verbose_name=b'Requirements', choices=[(b'University 1st degree', b'1'), (b'University 2nd degree', b'2'), (b'University 3rd degree', b'3')]),
        ),
        migrations.AlterField(
            model_name='job_position',
            name='language_requirements',
            field=models.CharField(max_length=20, verbose_name=b'Language requirements', choices=[(b'English - basic', b'EN-1'), (b'English advanced', b'EN-2'), (b'German - basic', b'DE-1'), (b'German - advanced', b'DE-2')]),
        ),
    ]
