# Generated by Django 5.0 on 2024-01-18 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_delete_st_course'),
    ]

    operations = [
        migrations.CreateModel(
            name='st_course',
            fields=[
                ('st_course_id', models.AutoField(primary_key=True, serialize=False)),
                ('course_id', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('course_name', models.CharField(max_length=100)),
                ('fees', models.CharField(max_length=100)),
                ('duration', models.CharField(max_length=100)),
                ('commencement_date', models.CharField(max_length=100)),
            ],
        ),
    ]
