# Generated by Django 2.0 on 2020-10-21 04:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cornelius_app', '0007_auto_20201021_1234'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='corneliususer',
            options={},
        ),
        migrations.RemoveField(
            model_name='corneliususer',
            name='created',
        ),
    ]
