# Generated by Django 4.0.6 on 2023-02-23 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0018_alter_habit_semester_alter_habitlog_habit'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='habit',
            name='semester',
        ),
        migrations.AlterField(
            model_name='habitlog',
            name='habit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='habit_track', to='home_app.habit'),
        ),
    ]
