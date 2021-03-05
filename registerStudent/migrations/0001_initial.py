# Generated by Django 3.1.4 on 2021-03-05 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RegisterStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='students/')),
                ('grade', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('fathersName', models.CharField(max_length=255)),
                ('phoneNumber', models.CharField(max_length=13)),
                ('studentId', models.IntegerField()),
            ],
        ),
    ]