# Generated by Django 4.1.2 on 2022-10-27 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0003_alter_habitlog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitlog',
            name='date',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
