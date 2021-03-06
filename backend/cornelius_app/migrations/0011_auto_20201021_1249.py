# Generated by Django 2.0 on 2020-10-21 04:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cornelius_app', '0010_auto_20201021_1245'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Patient',
        ),
        migrations.AlterField(
            model_name='doctor',
            name='did',
            field=models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cornelius_app.CorneliusUser'),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('pid', models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cornelius_app.CorneliusUser')),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('insurance', models.CharField(blank=True, max_length=50, null=True)),
            ],
            bases=('cornelius_app.corneliususer',),
        ),
        migrations.AlterField(
            model_name='Doctor',
            name='did',
            field=models.OneToOneField(db_column='uid', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='cornelius_app.CorneliusUser'),
        ),
        migrations.AlterField(
            model_name='DoctorPatientMeeting',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Patient'),
        ),
        migrations.AlterField(
            model_name='MeetingInfo',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Patient'),
        ),
    ]
