# Generated by Django 4.0.6 on 2022-12-20 07:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0010_alter_habitlog_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitlog',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
