# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-04-07 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [("talk", "0040_add_block_for_timeslot")]

    operations = [
        migrations.AlterModelOptions(
            name="talkslot",
            options={"verbose_name": "Talk slot", "verbose_name_plural": "Talk slots"},
        ),
        migrations.AlterUniqueTogether(name="talkslot", unique_together=set([])),
    ]
