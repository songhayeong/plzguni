# Generated by Django 3.2.15 on 2022-10-26 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0041_auto_20221026_1439'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuraldroptasks',
            name='Checkbox1',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
