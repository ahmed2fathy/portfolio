# Generated by Django 4.0.1 on 2022-01-18 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0014_alter_category_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='post_views',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
