# Generated by Django 3.0.5 on 2020-07-27 23:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blindchess', '0004_game_game_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='game_id',
        ),
    ]