# Generated by Django 4.0.6 on 2023-04-03 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0004_alter_forumaddlog_track_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='forumgroups',
            name='delete_time',
            field=models.DateField(default=None, null=True),
        ),
    ]