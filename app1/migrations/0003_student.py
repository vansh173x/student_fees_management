# Generated by Django 5.0 on 2024-01-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_operator'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('Name', models.CharField(max_length=100)),
                ('Gender', models.CharField(max_length=100)),
                ('Course', models.CharField(max_length=100)),
                ('Address', models.CharField(max_length=100)),
                ('Contact', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100, primary_key=True, serialize=False)),
            ],
        ),
    ]
