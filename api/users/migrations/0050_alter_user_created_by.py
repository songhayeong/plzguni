# Generated by Django 3.2.15 on 2022-10-30 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0049_task_state'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='created_by',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
