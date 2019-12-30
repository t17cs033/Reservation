# Generated by Django 3.0 on 2019-12-25 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpId', models.IntegerField()),
                ('amount', models.CharField(max_length=50)),
                ('remain', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fclName', models.CharField(max_length=50)),
                ('stock', models.CharField(max_length=50)),
                ('charge', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MeetingRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mrName', models.CharField(max_length=50)),
                ('avail', models.IntegerField()),
                ('charge', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cmpId', models.IntegerField()),
                ('cmpName', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=50)),
                ('section', models.CharField(max_length=50)),
                ('name', models.CharField(max_length=50)),
                ('mail', models.CharField(max_length=50)),
                ('pay', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
                ('cmpId', models.IntegerField()),
                ('date', models.DateField()),
                ('start_time', models.CharField(max_length=50)),
                ('end_time', models.CharField(max_length=50)),
                ('mrName', models.CharField(max_length=50)),
                ('fclName', models.CharField(max_length=50)),
                ('charge', models.CharField(max_length=50)),
            ],
        ),
    ]