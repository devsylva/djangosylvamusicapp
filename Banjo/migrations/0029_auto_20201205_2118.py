# Generated by Django 3.1.4 on 2020-12-05 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0028_auto_20201205_2113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
