# Generated by Django 4.1 on 2022-11-01 03:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0016_alter_comment_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 3, 35, 0, 169965, tzinfo=datetime.timezone.utc)),
        ),
    ]