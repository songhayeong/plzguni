# Generated by Django 3.2.15 on 2022-09-15 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_testingtasks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testingtasks',
            name='AiFilenametoCompress',
        ),
        migrations.RemoveField(
            model_name='testingtasks',
            name='Taskname',
        ),
        migrations.RemoveField(
            model_name='testingtasks',
            name='dateofuse',
        ),
    ]
