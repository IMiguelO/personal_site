# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20151022_1810'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='title',
            field=models.IntegerField(default=0, choices=[(0, b''), (1, b'Mr'), (2, b'Ms'), (3, b'Mrs'), (4, b'Dr'), (5, b'Seniora'), (6, b'Senior')]),
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
