# Generated by Django 3.1.2 on 2021-02-18 05:17

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20210217_2311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='posible_answers',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=50), blank=True, null=True, size=5),
        ),
    ]