# Generated by Django 4.0.6 on 2023-04-03 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum_app', '0008_previous_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='previous_group',
            name='winner_user',
            field=models.CharField(max_length=70, null=True),
        ),
    ]
