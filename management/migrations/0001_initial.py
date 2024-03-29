# Generated by Django 4.1.7 on 2023-03-26 07:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import management.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('txtReport', models.FileField(upload_to='static/AttendanceRecords')),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Hostel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostel_number', models.CharField(max_length=2)),
                ('warden', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_num', models.IntegerField()),
                ('wing', models.CharField(max_length=1)),
                ('floor', models.IntegerField()),
                ('capacity', models.IntegerField()),
                ('status', models.IntegerField(default=0)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('mail', models.CharField(max_length=30)),
                ('student_contact_num', models.BigIntegerField()),
                ('guardian_contact_num', models.BigIntegerField()),
                ('gender', models.CharField(max_length=1)),
                ('roll_num', models.ForeignKey(db_column='username', on_delete=management.models.Room, to=settings.AUTH_USER_MODEL, unique=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.room')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('hostel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.hostel')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
        migrations.CreateModel(
            name='ChangeRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reason', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='management.student')),
            ],
        ),
    ]
