# Generated by Django 4.0.6 on 2022-11-18 09:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_alter_video_video'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='video',
        ),
    ]
