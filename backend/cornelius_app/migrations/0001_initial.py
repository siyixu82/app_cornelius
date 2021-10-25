# Generated by Django 2.0 on 2020-10-10 07:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cornelius_User',
            fields=[
                ('uid', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('role', models.CharField(choices=[('P', 'Patient'), ('D', 'Doctor')], max_length=10)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=30)),
            ],
            options={
                'db_table': 'cornelius_user',
            },
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('did', models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Cornelius_User')),
            ],
            options={
                'db_table': 'doctor',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('fid', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'facility',
            },
        ),
        migrations.AddField(
            model_name='doctor',
            name='fid',
            field=models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Facility'),
        ),
    ]
