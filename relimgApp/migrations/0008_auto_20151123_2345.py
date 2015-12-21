# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0007_auto_20151121_1728'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='description',
            field=models.CharField(default=b'', max_length=10000, null=True, blank=True),
        ),
    ]
