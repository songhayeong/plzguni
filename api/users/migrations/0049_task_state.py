# Generated by Django 3.2.15 on 2022-10-28 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_file_task'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='state',
            field=models.CharField(default='upload', max_length=100),
        ),
    ]
