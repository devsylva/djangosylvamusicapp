# Generated by Django 3.1.2 on 2020-12-03 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banjo', '0007_event'),
    ]

    operations = [
        migrations.AlterField(
            model_name='music',
            name='file_location',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Music file directory'),
        ),
    ]
