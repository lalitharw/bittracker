# Generated by Django 4.0.6 on 2023-04-20 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0043_alter_habitlog_habit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habitlog',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit_track', to='home_app.habit'),
        ),
    ]
