# Generated by Django 4.0.1 on 2022-01-09 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0002_footerheader_about_link'),
    ]

    operations = [
        migrations.RenameField(
            model_name='footerheader',
            old_name='about_txt',
            new_name='Copyright',
        ),
        migrations.RenameField(
            model_name='footerheader',
            old_name='about',
            new_name='Copyright_date',
        ),
        migrations.RenameField(
            model_name='footerheader',
            old_name='about_link',
            new_name='Copyright_link',
        ),
        migrations.AddField(
            model_name='footerheader',
            name='Copyright_txt_1',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='footerheader',
            name='Copyright_txt_2',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
        migrations.AddField(
            model_name='footerheader',
            name='all_rights_reserved',
            field=models.CharField(blank=True, max_length=220, null=True),
        ),
    ]
