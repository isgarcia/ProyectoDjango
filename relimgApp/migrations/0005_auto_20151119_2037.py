# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0004_auto_20151119_0116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image_BD',
            field=models.URLField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
