# Generated by Django 3.1.2 on 2021-02-18 05:48

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0007_usercoursemodel'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserCourseModel',
            new_name='UserCourse',
        ),
    ]
