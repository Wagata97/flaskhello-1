# Generated by Django 3.0.10 on 2022-08-02 16:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0006_actors'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Actors',
            new_name='Actor',
        ),
    ]
