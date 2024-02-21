# Generated by Django 4.0.6 on 2023-03-27 13:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home_app', '0035_alter_habit_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='habit',
            name='icon',
            field=models.CharField(choices=[('fa-solid fa-user', 'GREEN'), ('blue', 'BLUE'), ('red', 'RED'), ('orange', 'ORANGE'), ('black', 'BLACK')], max_length=100),
        ),
    ]
