# Generated by Django 3.0.10 on 2022-08-01 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='description',
            field=models.CharField(default=None, max_length=256),
        ),
    ]
