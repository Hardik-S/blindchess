# Generated by Django 3.0.5 on 2020-07-27 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='losses',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='profile',
            name='rating',
            field=models.IntegerField(default=None),
        ),
        migrations.AddField(
            model_name='profile',
            name='wins',
            field=models.IntegerField(default=0),
        ),
    ]