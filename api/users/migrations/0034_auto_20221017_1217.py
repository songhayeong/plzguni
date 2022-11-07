# Generated by Django 3.2.15 on 2022-10-17 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0033_remove_neuraldroptasks_aifilenametocompress'),
    ]

    operations = [
        migrations.AddField(
            model_name='neuraldroptasks',
            name='Checkbox',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='neuraldroptasks',
            name='File',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='neuraldroptasks',
            name='FileType',
            field=models.CharField(default='file', max_length=50),
        ),
    ]