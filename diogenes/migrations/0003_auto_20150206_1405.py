# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('diogenes', '0002_auto_20150203_0048'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='clean_title',
            field=models.CharField(default='default', max_length=128, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.CharField(max_length=128, blank=True),
            preserve_default=True,
        ),
    ]
