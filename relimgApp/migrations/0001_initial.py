# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Anime',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default=b'', max_length=255)),
                ('condition', models.CharField(max_length=1, choices=[(b'E', b'In emission'), (b'F', b'Finished')])),
                ('type_anime', models.CharField(max_length=1, choices=[(b'O', b'OVA'), (b'F', b'Film'), (b'A', b'Anime')])),
                ('description', models.CharField(default=b'', max_length=10000)),
                ('image', models.ImageField(max_length=255, null=True, upload_to=b'C:\\Users\\Ismael\\Documents\\Proyectos Django\\relimg\\relimgApp/media', blank=True)),
                ('date', models.DateTimeField(verbose_name=b'date')),
            ],
        ),
        migrations.CreateModel(
            name='Categorie',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('categories', models.CharField(default=b'', max_length=255)),
                ('date', models.DateTimeField(verbose_name=b'date')),
                ('anime', models.ForeignKey(to='relimgApp.Anime')),
            ],
        ),
    ]
