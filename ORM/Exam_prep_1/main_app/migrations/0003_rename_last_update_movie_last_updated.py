# Generated by Django 4.2.4 on 2023-11-19 14:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_alter_movie_actors'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='last_update',
            new_name='last_updated',
        ),
    ]
