# Generated by Django 3.1.2 on 2020-12-04 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0012_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='comment',
            field=models.TextField(max_length=1000),
        ),
    ]
