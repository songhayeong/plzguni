# Generated by Django 3.2.15 on 2022-10-04 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_testingtasks_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testingtasks',
            name='Writing',
        ),
        migrations.AddField(
            model_name='testingtasks',
            name='FileType',
            field=models.CharField(default='file', max_length=50),
        ),
    ]
