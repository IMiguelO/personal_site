# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_question_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='description',
            new_name='message',
        ),
        migrations.RenameField(
            model_name='question',
            old_name='title',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='question',
            name='email',
            field=models.EmailField(max_length=254, null=True, blank=True),
        ),
    ]
