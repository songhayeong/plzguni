# Generated by Django 3.2.15 on 2022-09-01 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_delete_datafile'),
    ]

    operations = [
        migrations.DeleteModel(
            name='NeuralDropTask',
        ),
    ]
