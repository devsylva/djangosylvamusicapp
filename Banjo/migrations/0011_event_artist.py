# Generated by Django 3.1.2 on 2020-12-03 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0010_auto_20201203_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='artist',
            field=models.CharField(blank=True, max_length=40),
        ),
    ]