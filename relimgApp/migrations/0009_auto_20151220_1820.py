# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('relimgApp', '0008_auto_20151123_2345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anime',
            name='condition',
            field=models.CharField(max_length=1, choices=[(b'E', b'En emisi\xc3\xb3n'), (b'F', b'Finalizado')]),
        ),
        migrations.AlterField(
            model_name='anime',
            name='type_anime',
            field=models.CharField(max_length=1, choices=[(b'O', b'OVA'), (b'F', b'Pel\xc3\xadcula'), (b'A', b'Anime')]),
        ),
    ]
