# Generated by Django 3.0.4 on 2020-04-07 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0010_moveininfo_roomphoto'),
    ]

    operations = [
        migrations.AddField(
            model_name='moveininfo',
            name='roomstatus',
            field=models.IntegerField(default=0, max_length=30),
            preserve_default=False,
        ),
    ]
