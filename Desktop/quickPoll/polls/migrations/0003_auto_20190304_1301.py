# Generated by Django 2.1.5 on 2019-03-04 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_poll_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poll',
            name='text',
            field=models.CharField(max_length=255, null='DEFAULT VALUE'),
        ),
    ]
