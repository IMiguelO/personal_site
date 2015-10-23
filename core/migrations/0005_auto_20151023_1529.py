# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20151022_1821'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='message',
            new_name='question',
        ),
    ]
