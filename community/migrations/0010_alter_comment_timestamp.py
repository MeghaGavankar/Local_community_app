# Generated by Django 4.1 on 2022-10-31 14:35

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('community', '0009_comment_remove_queryanswer_service_provide_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='Timestamp',
            field=models.DateTimeField(default=datetime.datetime(2022, 10, 31, 14, 35, 23, 897139, tzinfo=datetime.timezone.utc)),
        ),
    ]
