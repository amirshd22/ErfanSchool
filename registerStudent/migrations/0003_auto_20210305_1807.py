# Generated by Django 3.1.4 on 2021-03-05 14:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registerStudent', '0002_auto_20210305_1740'),
    ]

    operations = [
        migrations.RenameField(
            model_name='registerstudent',
            old_name='studenImage',
            new_name='studentImage',
        ),
    ]
