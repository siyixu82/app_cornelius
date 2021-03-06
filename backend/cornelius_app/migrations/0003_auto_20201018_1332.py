# Generated by Django 2.0 on 2020-10-18 05:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('cornelius_app', '0002_auto_20201010_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='DoctorPatientMeeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('did', models.ForeignKey(db_column='did', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Doctor')),
            ],
            options={
                'db_table': 'doctor_patient_meeting',
            },
        ),
        migrations.CreateModel(
            name='MeetingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('reason', models.TextField()),
                ('did', models.ForeignKey(db_column='did', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Doctor')),
                ('fid', models.ForeignKey(db_column='fid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Facility')),
            ],
            options={
                'db_table': 'meeting_info',
            },
        ),
        migrations.CreateModel(
            name='MeetingScript',
            fields=[
                ('mid', models.AutoField(primary_key=True, serialize=False)),
                ('script', models.TextField()),
            ],
            options={
                'db_table': 'meeting_script',
            },
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50)),
                ('insurance', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'patient',
            },
        ),
        migrations.CreateModel(
            name='VisitJournal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('treatment', models.TextField()),
                ('diagonisis', models.TextField()),
                ('follow_up', models.TextField()),
                ('question', models.TextField()),
                ('medication', models.TextField()),
                ('notes', models.TextField()),
                ('cost', models.TextField()),
                ('pid', models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.MeetingScript')),
            ],
            options={
                'db_table': 'visit_journal',
            },
        ),
        migrations.AlterModelOptions(
            name='corneliususer',
            options={'ordering': ['created']},
        ),
        migrations.AddField(
            model_name='corneliususer',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient',
            name='pid',
            field=models.ForeignKey(db_column='uid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.CorneliusUser'),
        ),
        migrations.AddField(
            model_name='meetinginfo',
            name='mid',
            field=models.ForeignKey(db_column='mid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.MeetingScript'),
        ),
        migrations.AddField(
            model_name='meetinginfo',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Patient'),
        ),
        migrations.AddField(
            model_name='doctorpatientmeeting',
            name='pid',
            field=models.ForeignKey(db_column='pid', on_delete=django.db.models.deletion.DO_NOTHING, to='cornelius_app.Patient'),
        ),
    ]
