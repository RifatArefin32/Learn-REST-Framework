# Generated by Django 5.1.2 on 2024-10-23 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teacher_name', models.CharField(max_length=25)),
                ('course_name', models.CharField(max_length=20)),
                ('course_duration', models.IntegerField()),
                ('seat', models.IntegerField()),
            ],
        ),
    ]
