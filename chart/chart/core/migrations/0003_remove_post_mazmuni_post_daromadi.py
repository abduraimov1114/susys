# Generated by Django 4.0 on 2022-08-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_post_mazmuni'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='mazmuni',
        ),
        migrations.AddField(
            model_name='post',
            name='daromadi',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]
