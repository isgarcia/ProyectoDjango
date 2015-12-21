# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0006_auto_20151120_1824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='image_media',
            field=models.ImageField(max_length=255, null=True, upload_to=b'C:\\Users\\Ismael\\Documents\\Proyectos Django\\relimg\\relimgApp/static/images', blank=True),
        ),
    ]
