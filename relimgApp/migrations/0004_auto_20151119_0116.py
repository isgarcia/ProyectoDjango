# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0003_auto_20151118_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image_BD',
            field=models.CharField(default=b'', max_length=255, null=True, blank=True),
        ),
    ]
