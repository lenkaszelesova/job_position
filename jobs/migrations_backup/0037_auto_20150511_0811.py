# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0036_auto_20150511_0808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job_position',
            name='create_date',
            field=models.DateField(default=datetime.datetime(2015, 5, 11, 8, 11, 8, 815689, tzinfo=utc), verbose_name=b'Job created'),
        ),
    ]
