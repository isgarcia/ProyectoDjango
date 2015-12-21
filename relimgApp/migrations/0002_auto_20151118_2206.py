# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='anime',
            name='image',
        ),
        migrations.AddField(
            model_name='anime',
            name='image_BD',
            field=models.CharField(default=b'', max_length=255),
        ),
        migrations.AddField(
            model_name='anime',
            name='image_media',
            field=models.ImageField(max_length=255, null=True, upload_to=b'C:\\Users\\Ismael\\Documents\\Proyectos Django\\relimg\\media/', blank=True),
        ),
    ]
