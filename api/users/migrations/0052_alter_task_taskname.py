# Generated by Django 3.2.15 on 2022-10-31 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0051_auto_20221031_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='taskname',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
