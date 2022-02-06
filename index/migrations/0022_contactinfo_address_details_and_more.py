# Generated by Django 4.0.1 on 2022-02-06 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0021_contactinfo_alter_feedback_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactinfo',
            name='address_details',
            field=models.CharField(blank=True, max_length=90, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='address',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AlterField(
            model_name='contactinfo',
            name='work_time',
            field=models.CharField(blank=True, default='Mon to Fri 9am to 6 pm', max_length=70),
        ),
    ]
