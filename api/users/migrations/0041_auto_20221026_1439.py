# Generated by Django 3.2.15 on 2022-10-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0040_alter_neuraldroptasks_taskname'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testingtasks',
            old_name='Checkbox',
            new_name='Checkbox1',
        ),
        migrations.AddField(
            model_name='testingtasks',
            name='Checkbox2',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.CharField(default='', max_length=10),
        ),
    ]
