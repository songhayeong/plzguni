# Generated by Django 3.2.15 on 2022-09-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_rename_aifilepathtocompress_testingtasks_file'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingtasks',
            name='Writing',
            field=models.TextField(null=True),
        ),
    ]
