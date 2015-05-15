# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job_Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('job_name', models.CharField(max_length=300, verbose_name=b'Job name')),
                ('job_location', models.CharField(default=b'KE', max_length=100, choices=[(b'KE', b'Kosice'), (b'BA', b'Bratislava')])),
                ('create_date', models.DateField(default=datetime.datetime(2015, 5, 8, 8, 37, 31, 734775, tzinfo=utc), verbose_name=b'Job created')),
                ('start_date', models.DateField(verbose_name=b'Start date')),
                ('contract_type', models.CharField(default=b'FT', max_length=20, verbose_name=b'Contract type:', choices=[(b'FT', b'Full time'), (b'PT', b'Part time')])),
                ('job_description', models.TextField(verbose_name=b'Job job_description')),
                ('job_requirements', models.CharField(default=b'2', max_length=20, verbose_name=b'Requirements', choices=[(b'1', b'University 1st degree'), (b'2', b'University 2nd degree'), (b'3', b'University 3rd degree')])),
                ('pc_requirements', models.TextField(verbose_name=b'PC requirements')),
                ('language_requirements', models.CharField(default=b'EN-2', max_length=20, verbose_name=b'Language requirements', choices=[(b'EN-1', b'English - basic'), (b'EN-2', b'English - advanced'), (b'DE-1', b'German - basic'), (b'DE-2', b'German - advanced')])),
                ('other_requirements', models.TextField(verbose_name=b'Other requirements')),
                ('ness_info', models.TextField(default=b'About Ness KDC.', verbose_name=b'Information about the company')),
                ('highlighted', models.TextField()),
                ('owner', models.ForeignKey(related_name='jobs', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
