# Generated by Django 3.2.15 on 2022-08-31 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_auto_20220830_1741'),
    ]

    operations = [
        migrations.CreateModel(
            name='Datafile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DataNum', models.IntegerField()),
            ],
        ),
    ]
