# Generated by Django 4.2 on 2023-04-26 12:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0045_remove_profile_first_name_remove_profile_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitlog',
            name='date',
            field=models.DateField(default=datetime.date(2023, 4, 26)),
        ),
    ]
