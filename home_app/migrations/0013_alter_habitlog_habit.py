# Generated by Django 4.0.6 on 2022-12-24 09:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0012_alter_habitlog_track_unit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitlog',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_app.habit'),
        ),
    ]