# Generated by Django 4.0.1 on 2022-01-17 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_alter_category_des_alter_tag_des_alter_tag_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/blog/frontbage/category'),
        ),
    ]
