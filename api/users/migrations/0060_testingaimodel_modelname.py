# Generated by Django 3.2.15 on 2022-11-03 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0059_auto_20221102_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='testingaimodel',
            name='Modelname',
            field=models.CharField(max_length=10, null=True),
        ),
    ]